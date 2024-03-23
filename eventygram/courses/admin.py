from eventygram.courses.models import MainCategory, Category, SubCategory, Course, Review
from django.contrib import admin


@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'main_category',
    ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
    ]
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'creator',
        'title',
        'topic',
        'content',
        'language',
        'requirements',
        'price',
        'description',
        'location',
        'study_method',
        'level',
        'status',
        'subcategory',
    ]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'course',
        'rating',
        'comment',
        'date_posted',
    ]
