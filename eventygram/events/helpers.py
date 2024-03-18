from eventygram import settings
import os


def event_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, '_pics', filename)
