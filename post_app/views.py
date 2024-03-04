from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views module from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),  # Include URLs from the 'posts' app
]