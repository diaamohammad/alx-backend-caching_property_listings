from django.core.cache import cache
from .models import Property
import logging

# إعداد الـ Logger (اختياري لكن مفيد)
logger = logging.getLogger(__name__)

def get_all_properties():
    """
    Fetches all properties, using low-level cache.
    Cache key: 'all_properties'
    Timeout: 3600 seconds (1 hour)
    """
    # 1. محاولة جلب البيانات من الكاش
    queryset = cache.get('all_properties')
    
    if queryset is None:
        # 2. (Cache Miss) - البيانات غير موجودة، اجلبها من قاعدة البيانات
        logger.info("Cache miss: 'all_properties'. Fetching from DB.")
        queryset = Property.objects.all()
        
        # 3. تخزين البيانات في الكاش لمدة ساعة (3600 ثانية)
        cache.set('all_properties', queryset, 3600)
    else:
        # 4. (Cache Hit) - البيانات موجودة
        logger.info("Cache hit: 'all_properties'. Serving from cache.")
        
    return queryset