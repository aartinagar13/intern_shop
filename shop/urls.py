from django.urls import path
from .import views
from shop.views import ProductListView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('product/', views.prodct, name="Product"),
    path('search/', views.search, name="Search"),
    path('productview/<int:myid>', views.prodView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('addcart/<int:myid>', views.addcart, name="addcart"),
    path("product/",ProductListView.as_view()),
] 
