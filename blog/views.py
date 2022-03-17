from django.shortcuts import render

# Create your views here.
def index(request):#1
	#posts = Post.objects.order_by('-created_date')[:3]
	#context = {
	#'posts':posts,
	#}
	return render(request, 'index.html')