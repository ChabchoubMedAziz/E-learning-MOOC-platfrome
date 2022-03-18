from django.shortcuts import (
	render, get_object_or_404, redirect, reverse)
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q, Count
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
#from accounts.models import Account
from .models import Post, CategoryPost, Contact,Course,CourseViewCount
#from .forms import CommentForm, PostForm, CourseForm, ContactForm

# Create your views here.
def index(request):#1
	#posts = Post.objects.order_by('-created_date')[:3]
	#context = {
	#'posts':posts,
	#}
	return render(request, 'index.html')


def blog(request):#3
	category = CategoryPost.objects.all()
	#featured = Account.objects.filter(featured=True)
	posts = Post.objects.order_by('-created_date')
	post_list = Post.objects.all()

	paginator = Paginator(Post.objects.all(), 4)
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		paginated_queryset = paginator.page(page)
	except PageNotAnInteger:
		paginated_queryset = paginator.page(1)

	except EmptyPage:
		paginated_queryset = paginator.page(paginator.num_pages)


	context = {
	'queryset': paginated_queryset,
	'page_request_var': page_request_var,
	'posts':posts,
	'category':category,
	'featured':featured,
	}
	return render(request, 'blog.html',context)


def course_search(request):
	queryset =  Course.objects.all()
	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(title__icontains=query)).distinct()
	context = {'queryset':queryset}
	return render(request, 'course/course_search_results.html', context)

def course(request):#2
	courses =  Course.objects.filter(featured=True)[:6]
	detail = Course.objects.all()
	context = {
	'course':courses,
	'detail':detail,
	}
	return render(request, 'course/course.html', context)

def contact(request):
	contact = Contact.objects.all()
	filled  = False
	if request.method == 'POST':
		name_r = request.POST.get('name')
		email_r = request.POST.get('email')
		subject_r = request.POST.get('subject')
		message_r = request.POST.get('message')
		c = Contact(name=name_r, email=email_r, subject=subject_r, message=message_r)
		c.save()
		filled = True
	context = {
	'filled':filled
	}
	return render(request, 'contact.html', context)
@login_required
def course_detail(request, slug):
	objects = get_object_or_404(Course, slug=slug)

	if request.user.is_authenticated:
		CourseViewCount.objects.get_or_create(user=request.user, course=objects)

	context = {
	'objects':objects
	}
	return render(request, 'course/course_detail.html', context)


@login_required
def course_create(request):
	# user = request.user
	form = CourseForm(request.POST or None, request.FILES or None)
	author = Account.objects.get(user=request.user)
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			form.save()
			return redirect(reverse('blog:course-detail', kwargs={
				'slug': form.instance.slug
				}))
	context = {'form':form, }
	return render(request, 'course/course_create.html', context)

@login_required
def course_update(request, slug):
	course = get_object_or_404(Course, slug=slug)
	form = CourseForm(request.POST or None, request.FILES or None, instance=course)
	author = Account.objects.get(user=request.user)
	if request.method == 'POST':
		if form.is_valid():
			form.instance.author = author
			form.save()
			return redirect(reverse('blog:course-detail', kwargs={
				'slug': form.instance.slug
				}))
	context = {'form':form}
	return render(request, 'course/course_update.html', context)


class CourseDelete(LoginRequiredMixin, DeleteView):
	model  = Course
	template_name = 'course/course_delete.html'
	context_object_name = 'objects'
	success_url = reverse_lazy('blog:course-view')
