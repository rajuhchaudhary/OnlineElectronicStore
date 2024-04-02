from django.contrib import admin
from  .models import Customer,Product,Cart,Order_placed,Feedback,Payment

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','location','city','zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discount_price','description','brand','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(Order_placed)
class Order_placedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','order_date','status']

@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','message','admin_reply','status','created_at']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','card_number','cvv','expiry_date']