from django.contrib import admin
# أضف include
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # أضف هذا السطر
    # هذا يربط أي URL يبدأ بـ 'properties/' بملف urls.py داخل تطبيق properties
    path('properties/', include('properties.urls')), 
]