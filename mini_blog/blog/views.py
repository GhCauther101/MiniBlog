from django.shortcuts import render
from django.http import HttpResponse

posts = [
	{
		'author': "Authorname",
		'title': "Blog title",
		'content': "Somethin happened ... ?",
		'date_posted': "12 August 2025",
	},
	{
		'author': "Authorname2",
		'title': "Blog titleeqfdzzz",
		'content': "Somethin happened ... ?",
		'date_posted': "12 August 2025",
	},
	{
		'author': "Authorname3",
		'title': "Blog title222",
		'content': "Somethin happened ... ?",
		'date_posted': "12 August 2025",
	},
	{
		'author': "Authorname4",
		'title': "Blog title 444",
		'content': "Somethin happened ... ?",
		'date_posted': "12 August 2025",
	},
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})