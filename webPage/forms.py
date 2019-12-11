from django import forms
from django.contrib.auth.models import User
from .models import Blog, Comment, Question, Choice
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class createUser(forms.ModelForm):
	password_check = forms.CharField(max_length=20, widget=forms.PasswordInput())
	field_order = ['username', 'password', 'password_check']
	
	class Meta:
		model = User
		widgets = {'password':forms.PasswordInput}
		fields = ['username', 'password']

class loginUser(forms.ModelForm):
	class Meta:
		model = User
		widgets = {'password':forms.PasswordInput}
		fields = ['username', 'password']

class newBlog(forms.ModelForm):
	class Meta:
		model = Blog

		fields = ['title', 'author', 'body']

		widgets = {
		'title' : forms.TextInput(
			attrs={'class':'form-control', 'style':'width:100%', 'placeholder':'input title name..'}
			),
		'author' : forms.Select(
			attrs={'class':'custom-select'},
			),
		'body' : forms.CharField(widget=CKEditorUploadingWidget()),
		}
		
class BlogCommentForm(forms.ModelForm):
	class Meta:
		model = Comment

		fields = ['comment_textfield']
		widgets = {
			'comment_textfield' : forms.Textarea(attrs={'class' : 'form-control', 'rows' : 4, 'cols' : 40})
		}

class newPoll(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['question_text']
class newChoice(forms.ModelForm):
	class Meta:
		model = Choice
		fields = ['choice_text']