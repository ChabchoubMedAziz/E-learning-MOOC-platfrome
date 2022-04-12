from django import forms

from .models import  Course, Comment

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title','body','categories','image','caption','video']



class CommentForm(forms.ModelForm):
	content  = forms.CharField(label='', widget=forms.Textarea(attrs={
		'class': 'form-control',
		'placeholder': 'Type your comment',
		'id': 'username',
		'rows':'6'
		}))
	class Meta:
		model = Comment
		fields = ['content']

