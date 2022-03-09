from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Popular(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=100, null=True)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/image'

        def __str__(self):
            return self.image
        
    class Meta:
        verbose_name_plural = 'Popular'

class Gallery(models.Model):
    food_name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    def __str__(self):
        return self.food_name

    @property
    def imageURL(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/path/to/default/image'

        def __str__(self):
            return self.image
        
    class Meta:
        verbose_name_plural = 'Gallery'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property 
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Gallery, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total