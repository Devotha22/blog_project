from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router= DefaultRouter()
router.register('blogs', views.BlogViewset, basename= 'blogs')

urlpatterns = [
    path('blogapi/', include(router.urls)), 
     
   
]
