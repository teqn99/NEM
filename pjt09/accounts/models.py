from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#이미지킷 사용시(리사이징)
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import Thumbnail
#원본유지하고 썸네일도 함께 사용하려면?
from imagekit.models import ImageSpecField


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    # 회원정보수정( => 프로필수정 / 인스타처럼)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(null=True, blank=True, max_length=64)   #blank=True: 사용자가 입력하지 않아도 저장가능
    profile_photo = models.ImageField(null=True, blank=True, upload_to='uploaded_profile_photos/')
    bio = models.TextField(null=True, blank=True) #blank=True: 사용자가 입력하지 않아도 저장가능

    profile_photo_thumbnail = ImageSpecField(
        source = 'profile_photo',   #원본 이미지 필드명
        processors = [Thumbnail(200,200)],
        format = 'JPEG',
        options={'quality':90},
    )

    


