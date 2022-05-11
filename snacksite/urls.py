from django.contrib import admin
from django.urls import path, include

admin.site.site_header  =  "Administration Pizza Valentino"  
admin.site.site_title  =  "Administration Pizza Valentino"
admin.site.index_title  =  "Pizza Valentino Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls'))
]
