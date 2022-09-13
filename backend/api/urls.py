from django.urls import path

from orderapp.models import Order

from . import views

urlpatterns = [
    path('', views.GetRoutesView.as_view()),
    path('categories/', views.CategoryCRUDView.as_view()),
    path('products/', views.ProductCRUDView.as_view()),
    path('colors/', views.ColorCRUDView.as_view()),
    path('sizes/', views.SizeCRUDView.as_view()),
    path('orders/', views.OrderCRUDView.as_view()),
    path('accounts/login/', views.UserLoginView.as_view()),
    path('accounts/register/', views.UserRegisterView.as_view()),
    path('users/', views.UserListView.as_view())
]
