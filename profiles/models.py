from django.db import models
from django.contrib.auth.models  import User
# Create your models here.

#프로필 모델
class Profile(models.Model):
    #OneToOneField 필드로 User 한명당 하나만 필요하기 때문에 1:1 관계를 맺어줌
    #CASCADE 연쇄 삭제
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='no bio...')
    #upload_to='avatars' 이미지 경로
    avatar = models.ImageField(upload_to='avatars', default='nopicture.JPG')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        #admin page username 반환
        return f"Profile of {self.user.username}"
