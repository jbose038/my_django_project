# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .forms import createUser, loginUser, newBlog, BlogCommentForm, newPoll, newChoice
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Blog, Comment, Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.forms.formsets import formset_factory


# Create your views here.
def index(request):
	return render(request, 'index.html')

def base(request):
	return render(request, 'base.html')

def signup(request):
	if request.method == 'POST':
		form = createUser(request.POST)

		if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['password_check']:
			new_user = User.objects.create_user(username=form.cleaned_data['username'],
				password=form.cleaned_data['password'])
			new_user.save()
			
			return redirect('index')
		else:
			return redirect('signup')
	else:
		form = createUser()
		return render(request, 'signup.html', {'form':form})

def login_(request):
	if request.method == 'POST':
		form = loginUser(request.POST)
		id_ = request.POST['username']
		pw = request.POST['password']
		u = authenticate(username=id_, password=pw)
		
		if u:
			login(request, user=u)
			return redirect('home')
		else:
			return redirect('login')
	else:
		form = loginUser()
		return render(request, 'login.html', {'form':form})

def logout_(request):
	logout(request)
	return redirect('index')

def home(request):
	blogs = Blog.objects.all()
	return render(request, 'home.html', {'blogs':blogs})

def createBlog(request):
	if request.method == 'POST':
		form = newBlog(request.POST)

		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return redirect('newBlog')
	else:
		form = newBlog()
		return render(request, 'newBlog.html', {'form':form})

def detail(request, blog_id):
	blog_detail = get_object_or_404(Blog, pk=blog_id)
	comments = Comment.objects.filter(blog_id=blog_id)

	if request.method == 'POST':
		comment_form = BlogCommentForm(request.POST)

		if comment_form.is_valid():
			content = comment_form.cleaned_data['comment_textfield']

			print(content)

			return redirect('home')
		else:
			return redirect('home')
	else:
		comment_form = BlogCommentForm()

		context = {
		'blog_detail' : blog_detail,
		'comments' : comments,
		'comment_form' : comment_form
		}

	return render(request, 'detail.html', context)

def polls(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {'latest_question_list' : latest_question_list}


	return render(request, 'polls/index.html', context)

def poll_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def poll_result(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		print(request.POST['choice'])
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',
			{'question' : question,
			'error_message' : "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('poll_result', args=(question.id,)))

def createPoll(request):
	ChoiceSet = formset_factory(newChoice, extra=1, min_num=2, validate_min=True)
	if request.method == 'POST':
		form = newPoll(request.POST)
		formset = ChoiceSet(request.POST)

		if all([form.is_valid(), formset.is_valid()]):
			poll = form.save()
			for inline_form in formset:
				if inline_form.cleaned_data:
					choice = inline_form.save(commit=False)
					choice.question = poll
					choice.save()

			return redirect('polls')
		else:
			return redirect('newPoll')
	else:
		form = newPoll()
		formset = ChoiceSet()

		return render(request, 'polls/newPoll.html',
			{'form':form, 'formset':formset})