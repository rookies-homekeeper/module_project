from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings ####
# Create your models here.

class Stuff(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    detail=models.TextField(max_length=300)
    quantity=models.IntegerField(default=0)
    image=models.ImageField(upload_to="",blank=True,verbose_name='stuff_img')
    pub_date=models.DateTimeField()
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_stuffs', blank=True) ####
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name

    def delete_stuff(self):
        # 상품 삭제 로직 추가
        self.delete()