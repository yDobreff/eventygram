from django.core.validators import MinValueValidator, MaxValueValidator
from eventygram.courses.choices import STUDY_METHODS, COURSE_LEVELS
from eventygram.accounts.models import Profile
from django.db import models


class MainCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    main_category = models.ForeignKey(
        MainCategory,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return self.name


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

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
    )

    description = models.TextField()

    location = models.CharField(
        max_length=150,
    )

    study_method = models.CharField(
        max_length=40,
        choices=STUDY_METHODS,
    )

    level = models.CharField(
        max_length=20,
        choices=COURSE_LEVELS,
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    @property
    def avg_rating(self):
        reviews = self.review_set.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / len(reviews)
            return average_rating
        else:
            return None


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
