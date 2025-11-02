from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import Property
from django.views.decorators.cache import cache_page # استيراد cache_page

# تطبيق الكاش لمدة 15 دقيقة (60 ثانية * 15)
@cache_page(60 * 15)
def property_list(request):
    """
    View to list all properties.
    The response is cached for 15 minutes.
    """
    properties = Property.objects.all()
    # تحويل البيانات إلى قائمة بسيطة لإرسالها كـ JSON
    data = list(properties.values("title", "location", "price"))
    
    return JsonResponse(data, safe=False)