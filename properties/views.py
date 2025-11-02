

# تطبيق الكاش لمدة 15 دقيقة (60 ثانية * 15)
from django.shortcuts import render
from django.http import JsonResponse
# from .models import Property  <-- لم نعد بحاجة إليها مباشرة هنا
from django.views.decorators.cache import cache_page

# 1. استيراد الدالة الجديدة
from .utils import get_all_properties 

# @cache_page(60 * 15)  <-- (ملاحظة)
# بما أننا سنستخدم low-level cache، لم نعد بحاجة لـ @cache_page هنا
# يمكنك تركها أو حذفها، لكن المنطق الآن يتم داخل get_all_properties
# الأفضل حذفها ليعتمد على الكاش الجديد
# @cache_page(60 * 15) <-- قم بحذف أو تعليق هذا السطر

def property_list(request):
    """
    View to list all properties.
    Uses low-level caching via get_all_properties().
    """
    # 2. استخدام الدالة الجديدة
    properties = get_all_properties()
    
    # تحويل البيانات إلى قائمة بسيطة لإرسالها كـ JSON
    data = list(properties.values("title", "location", "price"))
    
    return JsonResponse(data, safe=False)