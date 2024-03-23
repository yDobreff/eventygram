from eventygram import settings
import os


def course_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_course_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, 'course_pics', filename)
