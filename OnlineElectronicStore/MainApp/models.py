from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator,MaxValueValidator

STATE_CHOICES = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Punjab', 'Punjab'),
    ('Haryana', 'Haryana'),
    ('Rajasthan', 'Rajasthan'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Delhi', 'Delhi'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Jammu And Kashmir', 'Jammu And Kashmir'),
    ('Telangana', 'Telangana'),
    ('Kerala', 'Kerala'),
    ('Tamil nadu', 'Tamil nadu'),
    ('Sikkim', 'Sikkim'),

)

CATEGORY_CHOICES = (
    ('Tv', 'Tv'),
    ('Laptop', 'Laptop'),
    ('Mobile', 'Mobile'),
    ('Smart Watch', 'Smart Watch'),
    ('Computer', 'Computer'),
    ('Camera', 'Camera'),
    ('Speaker', 'Speaker'),
    ('Tablet', 'Tablet'),

)

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Canceled', 'Canceled'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    city=models.CharField(max_length=60)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=12)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_price(self):
        return self.quantity * self.product.discount_price

class Order_placed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    @property
    def total_price(self):
        return self.quantity * self.product.discount_price

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    admin_reply = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=(
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted')
    ),default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    card_number=models.BigIntegerField()
    cvv =models.IntegerField()
    expiry_date=models.DateTimeField()
    price=models.FloatField(default=0.0)