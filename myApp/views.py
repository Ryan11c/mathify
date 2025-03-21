from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Q

#Mixin to add category data to all views
#I will inherit it in my class-based views
class CategoryMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat_menu"] = Category.objects.all()
        return context


#Handles searching for posts across multiple fields using Q from django.db.models
def Search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        items = Post.objects.filter(
            Q(title__icontains=searched) | 
            Q(body__icontains=searched) | 
            Q(category__icontains=searched) |
            Q(author__username__icontains=searched)
        )
        cat_menu = Category.objects.all()
        #Render the search results page
        return render(request, 'myApp/search.html', {
            'cat_menu': cat_menu,
            'searched': searched,
            'items': items,
        })
    else:
        #Render the search page with no results if not POST
        cat_menu = Category.objects.all()
        return render(request, 'myApp/search.html', {'cat_menu': cat_menu})


def HomeView(request):
    return render(request, 'myApp/home.html', {'cat_menu': Category.objects.all()})


def BinaryCalculator(request):
    return render(request, 'myApp/binary_calculator.html', {'cat_menu': Category.objects.all()})


def DerivativeCalculator(request):
    return render(request, 'myApp/derivative_calculator.html', {'cat_menu': Category.objects.all()})


def Integral(request):
    return render(request, 'myApp/integral.html', {'cat_menu': Category.objects.all()})


def RowReducer(request):
    return render(request, 'myApp/row_reducer.html', {'cat_menu': Category.objects.all()})


def About(request):
    return render(request, 'myApp/about.html', {'cat_menu': Category.objects.all()})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else: 
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class BlogView(CategoryMixin, ListView):
    model = Post
    template_name = 'myApp/blog.html'
    ordering = ['-post_date']
    #paginate: only 9 post shows up in one page. 
    paginate_by = 9


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.title().replace('-', ' '))
    cat_menu = Category.objects.all()
    return render(request, 'myApp/categories.html', {
        'cats': cats.title().replace('-', ' '),
        'category_post': category_post,
        'cat_menu': cat_menu
    })


class ArticleDetailView(CategoryMixin, DetailView):
    model = Post
    template_name = 'myApp/article_details.html'
    def get_context_data(self, *args, **kwargs):
        comments_with_pics = []
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        #Solved the issue with the profile picture not showing up in the comment section.
        #What I did was loop through all the comments and assign the profile pic url to that user
        #If there was no url, it would assign none. In the articl_detail.html, it would iterate over the comments_with_pics list.
        #If the comment has pfp, render it, if not, put the default pfp. EZ ! o.o
        for comment in post.comments.all():
            try:
                user = User.objects.get(username=comment.name)
                profile_pic = user.profile.profile_pic.url if user.profile.profile_pic else None
                user_liked = comment.likes.filter(id=self.request.user.id).exists()
            except User.DoesNotExist:
                profile_pic = None
                user_liked = False
            comments_with_pics.append({
                'comment': comment,
                'profile_pic': profile_pic,
                'likes_count': comment.comment_likes(),
                'user_liked': user_liked,
            })
        #Return everything
        context["total_likes"] = total_likes
        context["liked"] = liked
        context["comments_with_pics"] = comments_with_pics
        return context


class AddPost(CategoryMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myApp/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

def LikeCommentView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    liked = False
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
        liked = False
        messages.info(request, "You unliked a comment.")
    else:
        comment.likes.add(request.user)
        liked = True
        messages.success(request, "You liked a comment.")
    return HttpResponseRedirect(reverse('article_details', args=[comment.post.id]))


class AddComment(CategoryMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'myApp/add_comment.html'
    def form_valid(self, form):
        #Checking if the user has a profile!!!!
        try:
            self.request.user.profile
        except ObjectDoesNotExist:
            #Redirect to profile creation page if no profile for the user
            messages.warning(self.request, "You need to create a profile first before commenting.")
            return redirect('create_profile')  
        form.instance.post_id = self.kwargs['pk'] #This is what I needed to make the comment have the name of the user automatically
        if self.request.user.is_authenticated:
            form.instance.name = self.request.user.username
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})


class AddCategoryView(CategoryMixin, CreateView):
    model = Category
    template_name = 'myApp/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class UpdatePostView(CategoryMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'myApp/update_post.html'


class DeletePostView(CategoryMixin, DeleteView):
    model = Post
    template_name = 'myApp/delete_post.html'
    success_url = reverse_lazy('blog_view')

