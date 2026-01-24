from django import forms
from  blogs.models import Category,Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields=('title','category','feature_image','short_description','blog_body','status','is_featured')


class AddUserForm(UserCreationForm):
    # usercreationform by default this will give us the password field
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_superuser','is_staff','groups','user_permissions')
        
class EditUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_superuser','is_staff','groups','user_permissions')      