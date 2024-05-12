from main import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'password', 'first_name', 'last_name', 'place', 'date_of_birth', 'image', 'status']


class UserSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'place', 'date_of_birth', 'image', 'status']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'



class PressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Press
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['name', 'bio', 'career', 'place', 'date_of_birth', 'date_of_death', 'image', 'books']


class AuthorSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['name', 'date_of_birth', 'date_of_death', 'image']



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class BookSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['title', 'image', 'author']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'

        
class ReviewSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['content', 'rating']


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wishlist
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'














"""
CRUD for api, not to dashboad
            Create                  Read              Update              Delete                List
User         +                      +                    +                      +                 -
Category     -                      -                    -                      -                 +
Press        -                      -                    -                      -                 +
Author       -                      +                    -                      -                 +
Book         -                      +                    -                      -                 +
Review       +                      -                    -                      -                 +
Wishlist     +                      -                    -                      +                 +
Cart         +                      -                    -                      +                 +


"""