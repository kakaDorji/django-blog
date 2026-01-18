from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models  import Blog,Category
from django.db.models import Q





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

def blogs(req,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_blog':single_blog
    }
    return render(req,'blogs.html',context)


def search(req):
    keyword=req.GET.get('keyword')
    # match the keyword with blogs we will show the blog
    # also check the blog description and blog_body
    # we need to import Q so that we can do the or operator
    blogs=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword
    }
    return render(req,'search.html',context)