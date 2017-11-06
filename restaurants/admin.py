from django.contrib import admin
from .models import Restaurant


class RestaurantModelAdmin(admin.ModelAdmin):
	list_display = ["name","description","id"]
	search_fields = ["description","name"]
	list_filter = ["opening_time"]
	class Meta:
		model = Restaurant




admin.site.register(Restaurant, RestaurantModelAdmin)