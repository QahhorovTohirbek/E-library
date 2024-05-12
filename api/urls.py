from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register),
    path('login/', views.log_in),
    path('logout/', views.log_out),
    path('profile/', views.profile),
    path('category/', views.category),
    path('press/', views.press),
    path('author/', views.author),
    path('author-list/', views.author_list),
    path('book-detail/<int:pk>/', views.book_detail),
    path('book-list/', views.book_list),
    path('review-create/', views.review_create),
    path('review-list/', views.review_list),
    path('cart-create/', views.cart_create),
    path('cart-list/', views.cart_list),
    path('cart-delete/<int:pk>/', views.cart_delete),
    path('wishlist-create/', views.wishlist_create),
    path('wishlist-list/', views.wishlist_list),
    path('wishlist-delete/<int:pk>/', views.wishlist_delete),
]