from django.urls import path
import blog.views

app_name = 'blog'

urlpatterns = [
    path('',blog.views.index,name='index'),
    path('blog',blog.views.archive,name='archive'),
    path('blog/create',blog.views.create,name='create'),
]
