from eventygram import settings
import os


def event_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_event_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, 'event_pics', filename)


def get_price_range(price_range):
    if price_range == '0-50':
        return 0, 50
    elif price_range == '50-150':
        return 50, 150
    elif price_range == '150-500':
        return 150, 500
    elif price_range == '500-1500':
        return 500, 1000
    elif price_range == '1500+':
        return 1500, float('inf')
    else:
        return None, None
