from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def Search(request): #function to use the search bar, returns the category, searched, and items (title of the specific post)
    if request.method == "POST": 
        searched = request.POST.get('searched')
        items = Post.objects.filter(title__contains=searched)
        cat_menu = Category.objects.all()  
        return render(request, 'myApp/search.html', {
            'cat_menu': cat_menu, 
            'searched': searched,
            'items': items,
            })
    else:
        cat_menu = Category.objects.all()  
        return render(request, 'myApp/search.html', {'cat_menu': cat_menu})


def HomeView(request):
    cat_menu = Category.objects.all()  
    return render(request, 'myApp/home.html', {'cat_menu': cat_menu})


def BinaryCalculator(request):
    cat_menu = Category.objects.all()
    return render(request, 'myApp/binary_calculator.html', {'cat_menu': cat_menu})


def DerivativeCalculator(request):
    cat_menu = Category.objects.all()
    return render(request, 'myApp/derivative_calculator.html', {'cat_menu': cat_menu})


def Integral(request):
    cat_menu = Category.objects.all()
    return render(request, 'myApp/integral.html', {'cat_menu': cat_menu})


def RowReducer(request):
    cat_menu = Category.objects.all()
    return render(request, 'myApp/row_reducer.html', {'cat_menu': cat_menu})


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


class BlogView(ListView):
    model = Post
    template_name = 'myApp/blog.html'
    ordering = ['-post_date']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.title().replace('-', ' '))
    cat_menu = Category.objects.all()
    return render(request, 'myApp/categories.html', {
        'cats': cats.title().replace('-', ' '),
        'category_post': category_post,
        'cat_menu': cat_menu
    })


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'myApp/article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myApp/add_post.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'myApp/add_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk'] #This is what I needed to make the comment have the name of the user automatically
        if self.request.user.is_authenticated:
            form.instance.name = self.request.user.username
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})


class AddCategoryView(CreateView):
    model = Category
    template_name = 'myApp/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'myApp/update_post.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs) 
        context["cat_menu"] = cat_menu
        return context
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'myApp/delete_post.html'
    success_url = reverse_lazy('blog_view')

