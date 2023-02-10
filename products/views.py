from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from products.models import Products, Category
from products.forms import ProductForm

def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }
        return render(request, 'products/create_product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
          Products.objects.create(
            name = form.cleaned_data['name'],
            price = form.cleaned_data['price'],
            stock = form.cleaned_data['stock'],
            
          )
          context = {
            'message': 'Product created successfully'
          }
          
          return render(request, 'products/create_product.html', context=context)            
        else:
           
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'products/create_product.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Products.objects.filter(name__contains=search)
    else:
        products = Products.objects.all()
    #Para mostrar los productos los metemos en el contexto#
    context = {
        'products': products
    }
    return render(request, 'products/list_products.html', context=context)

class ProductUpdateView(UpdateView):
     model= Products
     template_name = 'products/update_products.html'
     success_url = '/products/list-products/'
     fields = '__all__'
   
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'products/delete_products.html'
    success_url = '/products/list-products/'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'categories/create_category.html'
    fields = '__all__'
    success_url = '/products/list-categories/'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    fields = '__all__'
    success_url = '/products/delete-category/'

class CategoryUpdateView(UpdateView):
     model= Category
     template_name = 'categories/update_category.html'
     success_url = '/products/list-categories/'
     fields = '__all__'

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories': all_categories,
    }
    return render(request,'categories/list_categories.html', context=context )