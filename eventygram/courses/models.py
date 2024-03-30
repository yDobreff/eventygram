from django.core.validators import MinValueValidator, MaxValueValidator
from eventygram.courses.helpers import course_pic_path
from eventygram.accounts.models import Profile
from eventygram.courses import choices
from django.db.models import Avg
from django.db import models
import os


class MainCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Main Categories"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"


class Course(models.Model):
    creator = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        related_name='course_creator',
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    topic = models.CharField(
        max_length=200,
    )

    content = models.TextField(
        null=True,
        blank=True,
    )

    language = models.CharField(
        max_length=50,
        choices=choices.COURSE_LANGUAGES,
    )

    requirements = models.TextField(
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    study_method = models.CharField(
        max_length=40,
        choices=choices.STUDY_METHODS,
    )

    level = models.CharField(
        max_length=20,
        choices=choices.COURSE_LEVELS,
    )

    status = models.CharField(
        choices=choices.COURSE_STATUS,
        null=True,
        blank=True,
        default='Active',
    )

    image = models.ImageField(
        upload_to=course_pic_path,
        blank=True,
        null=True,
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    students = models.ManyToManyField(
        Profile,
        blank=True,
        related_name='students'
    )

    instructors = models.ManyToManyField(
        Profile,
        blank=True,
        related_name='instructors',
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_instance = Course.objects.get(pk=self.pk)
            except Course.DoesNotExist:
                pass
            else:
                if old_instance.image != self.image and old_instance.image:
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    @property
    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']

    @property
    def get_price_display(self):
        if self.price == 0.0:
            return "Free"
        else:
            return "${:.2f}".format(self.price)


class Review(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
    )

    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
    )

    comment = models.TextField()

    date_posted = models.DateTimeField(
        auto_now_add=True
    )
