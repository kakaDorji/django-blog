
from django.contrib import admin
from django.urls import path,include
# cant have same views name so we need to put  blgoview
from blogs import views as Blogview
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name='home'),
   
    path("category/",include('blogs.urls')),
    path('blogs/<slug:slug>/',Blogview.blogs,name='blogs'),
    # search endpoint
    path('blog/search/',Blogview.search,name='search'),
     path('register/',views.register,name='register'),
     path('login/',views.login,name='login'),
     path('logout/',views.logout,name="logout")
  
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
