from core.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # author= serializers.HiddenField(default= serializers.CurrentUserDefault())
    class Meta:
        model= Post
        fields= ['title','content','date_posted','image','author']
        
        
    
