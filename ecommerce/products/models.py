from django.db import models

# class User(models.Model):
#     user_name = models.CharField(max_length=50, default="Moataz")
#     # products = models.ForeignKey(Product, on_delete=models.PROTECT)
#     # products = models.CharField()

class Category(models.Model):
    cat_name = models.CharField(max_length=50)

class Producer(models.Model):
    producer_name = models.CharField(max_length=255)
    
# Create your models here.
class Product(models.Model): # table
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="photos/%y/%m/%d", blank=True, null=True)
    # client_name = models.CharField(max_length=100, default='')
    # client_name = models.ForeignKey(User, on_delete=models.PROTECT)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, default=1)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return f"{self.name} : {self.price}"
    class Meta:
        verbose_name = "Mart Product"
        ordering = ['price']


        
# class Order(models.Model):
#     order_name = models.CharField(max_length=100)
#     order_id = models.CharField()
    
# class Transaction(models.Model):
#     transaction_order_id = models.OneToOneField(Order, on_delete=models.CASCADE)


    