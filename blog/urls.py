from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index-view' ),
    path('blog/', views.blog,  name='blog-view'),
    path('course/', views.course, name='course-view'),
    path('course_createe/', views.course_create, name='course-create'),
    path('course/<slug:slug>', views.course_detail, name='course-detail'),
    path('course_updatee/<slug:slug>', views.course_update, name='course-update'),
    path('course_deletee/<slug:slug>', views.CourseDelete.as_view(), name='course-delete'),
path('course-search/', views.course_search, name='course-search'),
]