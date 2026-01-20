from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from assignments.models import About,SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth



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


# pass this form and load here
def register(req):
    # load form
   
    if req.method=="POST":
       form=RegistrationForm(req.POST)
       if form.is_valid():
           form.save()
           return redirect('register')
       else:
           print(form.errors)

    else:
        form=RegistrationForm()
    context={
            'form':form
        }
    return render(req,'register.html',context)


def login(req):
    if req.method=='POST':
         # using default authentication form
         form=AuthenticationForm(req,data=req.POST )
         if form.is_valid():
            #  get the username form database
             username=form.cleaned_data['username']
             password=form.cleaned_data['password']

             user=auth.authenticate(username=username,password=password)
             if user is not None:
                auth.login(req,user)
                return redirect('home')    

    else:
        form=AuthenticationForm(req )  
    context={
                'form':form
            }
    return render(req,'login.html',context)

def logout(req):
    auth.logout(req)
    return redirect('home')
