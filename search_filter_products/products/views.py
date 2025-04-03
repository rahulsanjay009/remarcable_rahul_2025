import json
from django.http import JsonResponse
from .models import Product, Category, Tag
from django.db.models import Q
from rest_framework.decorators import api_view
from django.shortcuts import render

#Converting the query set to python object
def normalize_json(products):
    products_list = []
    for product in products:
        products_list.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": float(product.price),  
            "image_url": product.image_url,
            "category": {
                "id": product.category.id if product.category else None,
                "name": product.category.name if product.category else "No Category",
            } if product.category else None,
            "tags": [{"id": tag.id, "name": tag.name} for tag in product.tags.all()],
        })
    return products_list

@api_view(["GET"])
def get_tags_categories(request):
    categories = list(Category.objects.all().values())
    tags = list(Tag.objects.all().values())
    
    categories_tags = { "categories" : categories, "tags": tags}
    return JsonResponse(categories_tags, safe=False)

@api_view(["POST"])
def get_products(request):
    data = json.loads(request.body)
    categories_filter = data.get("categoriesFilter",[]) if data else None
    tags_filter = data.get("tagsFilter",[]) if data else None
    tag_queries = Tag.objects.filter(name__in=tags_filter) if tags_filter else None
    query_set = Product.objects.all()
    if categories_filter:
        query_set = query_set.filter(category__name__in=categories_filter)
    if tag_queries:
        query_set = query_set.filter(tags__in = tag_queries)
    products_list = normalize_json(query_set.distinct())
    return JsonResponse(products_list, safe = False)

@api_view(["POST"])
def search_products(request):
    data = json.loads(request.body)
    search_text = data.get("searchText",[])
    print(search_text)
    products = Product.objects.filter(Q(name__icontains = search_text) | Q(description__icontains = search_text))  

    product_list  = normalize_json(products)
    return JsonResponse(product_list,safe=False)
    

def react_app(request):
    return render(request, 'index.html')