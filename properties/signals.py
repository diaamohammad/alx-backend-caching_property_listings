from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property
import logging

logger = logging.getLogger(__name__)

# هذا هو "المستقبل" الذي يستمع للإشارات
# نربطه بإشارتي post_save و post_delete
@receiver(post_save, sender=Property)
@receiver(post_delete, sender=Property)
def invalidate_property_cache(sender, instance, **kwargs):
    """
    Invalidates (deletes) the 'all_properties' cache key
    whenever a Property instance is saved or deleted.
    """
    logger.info(f"Signal received from {instance}. Invalidating 'all_properties' cache.")
    
    # السطر الأهم: حذف الكاش
    cache.delete('all_properties')