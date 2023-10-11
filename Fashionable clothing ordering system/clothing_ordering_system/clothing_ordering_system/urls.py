from django.contrib import admin
from django.urls import path, include
from clothing import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_list),
]
