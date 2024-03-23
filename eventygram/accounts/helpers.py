from eventygram.accounts import models
from eventygram import settings
import os


def profile_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.id}_profile_pic.{ext}"
    return os.path.join(settings.MEDIA_ROOT, 'profile_pics', filename)


def profile_picture_change(profile, new_profile_picture):
    try:
        old_instance = models.Profile.objects.get(pk=profile.pk)
    except models.Profile.DoesNotExist:
        pass
    else:
        if old_instance.profile_picture != profile.profile_picture:
            if old_instance.profile_picture:
                if os.path.isfile(old_instance.profile_picture.path):
                    os.remove(old_instance.profile_picture.path)

    profile.profile_picture = new_profile_picture
    profile.save(update_fields=['profile_picture'])
