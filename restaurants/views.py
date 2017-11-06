from django.shortcuts import render, get_object_or_404
from .models import Restaurant

def restaurant_list(request):
	objects = Restaurant.objects.all()
	context = {
	"restaurant_items": objects,
	} 
	return render(request, 'restaurant_list.html', context)



def restaurant_detail(request,restaurant_id):
	item = get_object_or_404(Restaurant, id=restaurant_id)
	context = {
	"item": item,
	} 
	return render(request, 'restaurant_detail.html', context)
