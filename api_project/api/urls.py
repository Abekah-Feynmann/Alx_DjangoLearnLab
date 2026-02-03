from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    #Route for BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    #Include Router urls for BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    #A mechanism for users to obtain a token given their username and password
    path('api-token-auth/', views.obtain_auth_token),

]