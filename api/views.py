from . import serializers
from main import models
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = models.User.objects.create_user(**serializer.validated_data)
            token, created = Token.objects.get_or_create(user=user)
            
            response_data = {
                'user': serializer.data,
                'token': token.key
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
    

@api_view(['POST'])
def log_in(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.User.objects.filter(username=username).first()
        if user is None:
            return Response({'error': 'User not found'}, status=404)
        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=400)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful', 'token': token.key}, status=200)
    

@api_view(['POST'])
def log_out(request):
    if request.method == 'POST':
        token = Token.objects.get(user=request.user).delete()
        return Response({'message': 'Logout successful'}, status=200)


@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    if request.method == 'GET':
        user = request.user
        serializer = serializers.UserSerializerList(user)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def category(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True)
        return Response(serializer.data)

    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def press(request):
    if request.method == 'GET':
        press = models.Press.objects.all()
        serializer = serializers.PressSerializer(press, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def author(request):
    if request.method == 'GET':
        authors = models.Author.objects.all()
        serializer = serializers.AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def author_list(request):
    if request.method == 'GET':
        authors = models.Author.objects.all()
        serializer = serializers.AuthorSerializerList(authors, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def book_detail(request, pk):
    if request.method == 'GET':
        book = models.Book.objects.filter(pk=pk).first()
        if book is None:
            return Response({'error': 'Book not found'}, status=404)
        serializer = serializers.BookSerializer(book)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def book_list(request):
    if request.method == 'GET':
        books = models.Book.objects.all()
        serializer = serializers.BookSerializerList(books, many=True)
        return Response(serializer.data)


@api_view(['POST','GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request):

    if request.method == 'POST':
        serializer = serializers.ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = models.Review.objects.all()
        serializer = serializers.ReviewSerializerList(reviews, many=True)
        return Response(serializer.data)
    


@api_view(['POST','GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def cart_create(request):
    if request.method == 'POST':
        serializer = serializers.CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    
    if request.method == 'GET':
        carts = models.Cart.objects.all()
        serializer = serializers.CartSerializer(carts, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def cart_list(request, pk):
    if request.method == 'GET':
        cart = models.Cart.objects.filter(pk=pk).first()
        if cart is None:
            return Response({'error': 'Cart not found'}, status=404)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)
    

@api_view(['POST'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def cart_delete(request, pk):
    cart = models.Cart.objects.filter(pk=pk).first()
    if cart is None:
        return Response({'error': 'Cart not found'}, status=404)
    cart.delete()
    return Response({'message': 'Cart deleted'})
    

@api_view(['POST','GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_create(request):
    if request.method == 'POST':
        serializer = serializers.WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'GET':
        wishlists = models.Wishlist.objects.all()
        serializer = serializers.WishlistSerializer(wishlists, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_list(request, pk):
    if request.method == 'GET':
        wishlist = models.Wishlist.objects.filter(pk=pk).first()
        if wishlist is None:
            return Response({'error': 'Wishlist not found'}, status=404)
        serializer = serializers.WishlistSerializer(wishlist)

        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def wishlist_delete(request, pk):
    wishlist = models.Wishlist.objects.filter(pk=pk).first()
    if wishlist is None:
        return Response({'error': 'Wishlist not found'}, status=404)
    wishlist.delete()
    return Response(status=204)
