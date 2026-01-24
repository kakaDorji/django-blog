from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    # category crud
    path('categories/',views.categories,name='categories'),
    path('categories/add/',views.add_category,name='add_category'),
    path('categories/edit/<int:pk>/',views.edit_categories,name='edit_categories'),
    path('categories/delete/<int:pk>/',views.delete_categories,name='delete_categories'),
    # blog post crud
    path('posts/',views.posts,name='posts'),
    path('posts/add/',views.add_post,name='add_post'),
    path('posts/edit/<int:pk>/',views.edit_post,name='edit_post'),
     path('posts/delete/<int:pk>/',views.delete_post,name='delete_post'),

    #  user crud
    path('users/',views.users,name='users'),
     path('users/add',views.add_users,name='add_users'),
      path('users/edit/<int:pk>/',views.edit_users,name='edit_users'),
      path('users/delete/<int:pk>/',views.delete_users,name='delete_users')

]
