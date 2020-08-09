from django.db import models
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

CATEGORY_CHOICES = (
    ('S', 'SmartPhone'),
    ('L', 'Laptop'),
    ('D', 'Desktop'),
    ('W', 'Watch'),
    ('H', 'HeadPhone'),
    ('T', 'Telivision'),
    ('C', 'Camera')
)
AVAILABILITY_PRODUCT = (
    ('In Stock', 'In Stock'),
    ('Out Of Range', 'Out Of Range'),
    ('Limited Stock', 'Limited Stock')
)
class product(models.Model):
    product_name = models.CharField(max_length=30)
    discount_price = models.IntegerField()
    final_price = models.IntegerField()
    product_desc = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    availabily = models.TextField(choices=AVAILABILITY_PRODUCT, max_length=15)
    product_img1 = models.ImageField(upload_to='Images')
    product_img2 = models.ImageField(upload_to='Images')

    def __str__(self):
        return self.product_name


class imageslider(models.Model):
    image_name = models.CharField(max_length=30)
    slider_img = models.ImageField(upload_to='Images')
    text1 = models.CharField(max_length=90)
    text2 = models.CharField(max_length=90)

    def __str__(self):
        return self.image_name

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_on =models.DateTimeField(auto_now_add=True, null=True)
    update_on = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Order (models.Model):
    cust_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_ids = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username


@receiver (post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= None, created= False, **kwargs):
    if created:
        Token.objects.create(user=instance)