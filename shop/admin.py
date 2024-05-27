from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import Product,Contact,Login_Activity,Orders,OrderUpdate

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Login_Activity)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
