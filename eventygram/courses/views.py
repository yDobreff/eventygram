from eventygram.courses.models import MainCategory, SubCategory, Review, Course
from eventygram.courses.forms import CourseCreateForm, CourseUpdateForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
        form = CourseCreateForm()

        context = {
            'form': form
        }

        return render(request, 'courses/course_create.html', context)

    def post(self, request):
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            form.save_m2m()
            course.instructors.add(request.user)
            return redirect('successful_course_registration', pk=course.pk)
        else:
            context = {
                'form': form,
            }
            return render(request, 'courses/course_create.html', context)


def successful_course_registration(request, pk):
    course = get_object_or_404(Course, pk=pk)

    context = {
        'course': course,
    }

    return render(request, 'courses/successful_course_registration.html', context)


def course_details(request, pk):
    course = get_object_or_404(Course, pk=pk)
    reviews = Review.objects.all()

    context = {
        'course': course,
        'reviews': reviews,
    }

    return render(request, 'courses/course_details.html', context)


@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseUpdateForm(instance=course)

    if request.user != course.creator:
        return redirect('courses_catalogue')

    if request.method == "POST":
        form = CourseUpdateForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_details', pk=course.pk)

    context = {
        'form': form,
        'course': course,
    }

    return render(request, 'courses/course_update.html', context)


@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('courses_catalogue')

    context = {
        'course': course,
    }

    return render(request, 'courses/course_delete.html', context)