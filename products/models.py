from django.db import models

# Create your models here.

#제품 모델
class Product(models.Model):
    name = models.CharField(max_length=120)
    #upload_to='products' 경로에 이미지 저장
    image = models.ImageField(upload_to='products', default='no_picture.JPG')
    price = models.FloatField(help_text='원화')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        #이렇게 return 해주면 admin 페이지에 상품명/일/월/년 으로 표기됨
        return f"{self.name}-{self.created.strftime('%d/%m/%Y')}"
