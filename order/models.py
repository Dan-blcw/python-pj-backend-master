from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='orders', through='OrderDetail')
    sku = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    total_amount = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def update_status(self, new_status):
        self.status = new_status
        self.save()

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_details', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    colors = models.CharField(max_length=30)
    size = models.CharField(max_length=30)