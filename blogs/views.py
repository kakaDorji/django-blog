from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models  import Blog,Category




# Create your views here.
def posts_by_category(req,category_id):
    # fetch te posts that belongs to the category with the id category_id + status is publised
    posts=Blog.objects.filter(status="Published",category=category_id)
    # to get the actual value of category not the number
    # if the category doestnot exist then we have error so we neen dto get object 404
    # category=Category.objects.get(pk=category_id)
    category=get_object_or_404(Category,pk=category_id)
# when we want to do some action that time we need to used try and catch blog

    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')    
    context={
        'posts':posts,
        'category':category
    }

    return render(req,'posts_by_category.html',context)
