from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,BlogForm
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def dashboard(req):
    category_count=Category.objects.all().count()
    blogs_count=Blog.objects.all().count()
    context={
       'blogs_count':blogs_count,
       'category_count':category_count 
    }
    return render(req,'dashboard/dashboard.html',context)


def categories(req):
    return render(req,'dashboard/categories.html')

def add_category(req):
    if req.method == 'POST':
       form=CategoryForm(req.POST)
       if form.is_valid():
           form.save()
           return redirect('categories')
           
    else:
        form=CategoryForm()
        context={
            'form':form
        }
    return render(req,'dashboard/add_category.html',context)


def edit_categories(req,pk):
    category=get_object_or_404(Category,pk=pk)
    if req.method == 'POST':
        # we are taking new value and old value
        form=CategoryForm(req.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    else:    
        form=CategoryForm(instance=category)
#  we are passing category so that we can  get the id of the category.

    context={
        'form':form,
        'category':category
    }
    return render(req,'dashboard/edit_category.html',context)

def delete_categories(req,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


# return all post
def posts(req):
    posts=Blog.objects.all()
    context={
        'posts':posts
    }
    return render(req,'dashboard/posts.html',context)

def add_post(req):
    if req.method=="POST":
    #    get all the form data: this how we get the data
    # all the text data will be go into req.post and for the file and image part we need to store in the req.files
       form=BlogForm(req.POST,req.FILES)
       if form.is_valid():
        #   before we save the custom form we need to save that fields
          post=form.save(commit=False)   #not pushing to the db 
          post.author=req.user  #getting the current loggin user
        #   we will take title and sluggy flied
          post.save()  #to get the id so that we can make it unique
        #   we will take title from req using clean data
          title=form.cleaned_data['title']
          post.slug=slugify(title) + '-' + str(post.id) # to make slug unique we are making this ..but we dont have post id aviable so how do we do that we need to save before to access the post.id
          post.save()
          return redirect('posts')
       else:
           print('form is not valid')
           print(form.errors)        
    else:    
        form=BlogForm()
    context={
        'form':form
    }
    return render(req,'dashboard/add_post.html',context)


def edit_post(req,pk):
    post=get_object_or_404(Blog,pk=pk)
    if req.method=='POST':
        # to accept both files and data as are doing edit we need to give instance as it is existing data
        form=BlogForm(req.POST,req.FILES,instance=post)
        if form.is_valid():
           post= form.save()
           title=form.cleaned_data['title']
           post.slug=slugify(title) + '-'+ str(post.id)
           post.save()
           return redirect('posts')
    else:    
    
    # how we prefill data=instance
        form=BlogForm(instance=post)
    context={
        'form':form,
        'post':post

    }
    
    return render(req,'dashboard/edit_post.html',context)
    

def delete_post(req,pk):
    post=get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')