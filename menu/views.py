from django.shortcuts import render, render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib.auth.models import User


class CategoryListView(ListView):
    model = Category
    template_name = 'menu/catprodlist.html' 


    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['category_product_list'] = Category.objects.add_related_count(Category.objects.all(), Product,'category','o_count',cumulative=True)
        cat_pr_dict = {}
        for ca in context['category_product_list']:
            pc = Product.objects.filter(category=ca)
            cat_pr_dict[ca.id] = pc
        context['prd3'] = cat_pr_dict 
        return context


def cat_new(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Revelmenu')
    else:
        form = CategoryForm()
    return render(request, 'menu/category_edit.html', {'form': form})

def cat_edit(request, pk):
    ctg = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=ctg)
        if form.is_valid():
            form.save()
            return redirect('Revelmenu')
    else:
        form = CategoryForm(instance=ctg)
    return render(request, 'menu/category_edit.html', {'form': form})


def prod_new(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Revelmenu')
    else:
        form = ProductForm()
    return render(request, 'menu/product_edit.html', {'form': form})

def prod_edit(request, pk):
    prd = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=prd)
        if form.is_valid():
            form.save()
            return redirect('Revelmenu')
    else:
        form = ProductForm(instance=prd)
    return render(request, 'menu/product_edit.html', {'form': form})


# Create your views here.


