from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def restaurant_list(request):
	objects = Restaurant.objects.all()
	paginator = Paginator(objects, 2)
	number = request.GET.get('page')

	try:
		objects = paginator.page(number)
	except PageNotAnInteger:
		objects = paginator.page(1)
	except EmptyPage:
		objects = paginator.page(paginator.num_pages)
	
	context = {
	"restaurant_items": objects,
	} 
	return render(request, 'restaurant_list.html', context)



def restaurant_detail(request,restaurant_id):
	item = get_object_or_404(Restaurant, id=restaurant_id)
	context = {
	"item": item,
	} 
	return render(request,'restaurant_detail.html', context)

def restaurant_create(request):
	form = RestaurantForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		messages.success(request,"Hey, you just added a restaurant!")
		return redirect("restaurant_list")
	context = {
	'form': form
	}
	return render(request,"restaurant_create.html", context) 

def restaurant_update(request, restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id)

	form = RestaurantForm(request.POST or None, request.FILES or None, instance=item)

	if form.is_valid():
		form.save()
		messages.info(request,"Hey, you just changed a restaurant!")
		return redirect("restaurant_list")
	context = {
	'form': form,
	'item': item,
	}
	return render(request,"restaurant_update.html", context)

def restaurant_delete(request, restaurant_id):
	Restaurant.objects.get(id=restaurant_id).delete()
	messages.warning(request, "Your business is closed:(")
	return redirect("restaurant_list")


