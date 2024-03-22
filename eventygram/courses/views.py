from eventygram.courses.models import MainCategory, Category, SubCategory, Review, Course
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from eventygram.courses.forms import CourseCreateForm
from django.views import View


class CoursesCatalogueView(View):
    def get(self, request, *args, **kwargs):
        main_categories = MainCategory.objects.all()

        context = {
            'main_categories': main_categories,
        }

        return render(request, 'courses/courses_catalogue.html', context)


def topic_view(request, pk):
    topic = get_object_or_404(SubCategory, pk=pk)

    context = {
        'topic': topic,
    }

    return render(request, 'courses/topic_view.html', context)


class CourseCreateView(LoginRequiredMixin, View):
    def get(self, request):
        # main_categories = MainCategory.objects.all()
        # categories = Category.objects.all()
        # subcategories = SubCategory.objects.all()

        form = CourseCreateForm()

        context = {
            # 'main_categories': main_categories,
            # 'categories': categories,
            # 'subcategories': subcategories,
            'form': form,
        }

        return render(request, 'courses/course_create.html', context)

    def post(self, request):
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            form.save()
            form.save_m2m()
        else:
            context = {
                'form': form,
            }
            return render(request, 'courses/course_create.html', context)


def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    reviews = Review.objects.all()

    context = {
        'course': course,
        'reviews': reviews,
    }

    return render(request, 'courses/course_details.html', context)
