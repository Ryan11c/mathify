#from . import views
from django.urls import path
from .views import HomeView, BlogView, ArticleDetailView, AddPost, AddComment, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, BinaryCalculator, DerivativeCalculator, RowReducer, Integral

urlpatterns = [
    path('', HomeView, name='home'),
    path('explore/', BlogView.as_view(), name="blog_view"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('article/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/remove/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('binary-calculator/', BinaryCalculator, name='binary_calculator'),
    path('derivative-calculator/', DerivativeCalculator, name='derivative_calculator'),
    path('integral-calculator/', Integral, name='integral_calculator'),
    path('row-reducer/', RowReducer, name='row_reducer'),
]