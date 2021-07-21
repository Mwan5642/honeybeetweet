from django.db import models
from django.utils.timezone import localtime

from cloudinary.models import CloudinaryField


class Post(models.Model):
    class Meta(object): 
        db_table = 'post'
    
    name = models.CharField(
    'Name', blank=False, null=False, max_length= 25, db_index=True, default='New Bee'
    )    
    body = models.CharField(
    'Body', blank=True, null=True, max_length= 140, db_index=True 
    )
    created_at = models.DateTimeField(
    'Created DateTime', blank=True, default= localtime
    )

    
    
    like_count = models.PositiveIntegerField(
        'like', default=0, blank=True
    )
    image = CloudinaryField('image', blank=True)