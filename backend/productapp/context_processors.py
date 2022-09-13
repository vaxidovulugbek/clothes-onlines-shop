from productapp.models import Category, Product
from django.views.generic import edit
from django.views.generic import ListView

# class ListCategoriesView(ListView):
#     model = Category
#     def get_queryset(self):
#         return super().get_queryset()

def getCategories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return context


def getTrandyProducts(request):
    products_t = Product.objects.filter(status='trandy')
    context = {'products_t': products_t}
    return context


def getArrivedProducts(request):
    products_a = Product.objects.filter(status='arrived')
    context = {'products_a': products_a}
    return context
