from django.shortcuts import render
from blogs.models import Category,Blog
from assignments.models import About,SocialLink
def home(req):
    # get all the category from db
  
    featured_posts=Blog.objects.filter(is_featured=True,status="Published")
    posts=Blog.objects.filter(is_featured=False,status="Published")
    # fetch about us
    try:
        about=About.objects.get()
        

    except:
        about=None 
          

    context={
        
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
      
    }
    return render(req,'home.html',context)

