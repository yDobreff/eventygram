from eventygram import settings
import os


def profile_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_profile_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, 'profile_pics', filename)
