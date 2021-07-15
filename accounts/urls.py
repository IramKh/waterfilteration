from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name=("main")),
    path('index.html/',views.home, name=("index")),
    path('products.html/',views.products, name=("products")),
    
    path('contact.html/',views.contact, name=("contact")),
    path('blog.html/',views.blog, name=("blog")),
    path('blog-post.html/',views.blog_post, name=("blog-post")),
    path('checkout.html/',views.checkout, name=("checkout")),
    path('terms.html/',views.terms, name=("terms")),
    path('about.html/',views.about, name=("about")),
    path('testimonials.html/',views.testimonials, name=("testimonials") ),
    path('cu.html/',views.about, name=("about")),
    path('about.html/',views.about, name=("about")),
    path('CustomerUpdate/<str:pk>', views.CustomerUpdate, name=("CustomerUpdate")),
    path('CustomerDelete/<str:pk>', views.CustomerDelete, name=("CustomerDelete")),
    path('messages', views.messages, name=("messages")),

    path('product_details/<str:id>', views.product_details, name='product_details'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('store', views.store, name='store'),
    path('Login/',views.Login, name='Login'),

]
