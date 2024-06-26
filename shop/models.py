from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length = 80)
    category = models.CharField(max_length=100,default=0)
    subcategory = models.CharField(max_length=200,default=0)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length = 300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images/",default="")
    
    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 80)
    email= models.CharField(max_length=100,default=0)
    phone =models.CharField(max_length=10,default=0)
    desc = models.CharField(max_length = 300,default=0)

    def __str__(self):
        return self.name
    
class Login_Activity(models.Model):
    username=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)    

    def __str__(self):
        return self.username  
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111, default=None)

    def __str__(self):
        return self.order_id

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    
class AddCart(models.Model):
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111)
    number=models.CharField(max_length=111)
    itemno=models.CharField(max_length=111)
    utem_name=models.CharField(max_length=111)  

    def __str__(self):
        return self.username  

