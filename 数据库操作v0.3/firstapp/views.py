from django.shortcuts import render, redirect
from firstapp.models import Article, Comment
from firstapp.forms import CommentForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    article_list = Article.objects.all()
    context = {}
    context["article_list"] = article_list
    return render(request, 'index.html', context)

def add(request):

    if request.method == "GET":
        form = CommentForm

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            content = form.cleaned_data["content"]
            c = Comment(name=name, content=content)
            c.save()
            return redirect(to="add")

    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'add.html', context)

def delete(request, pk):
    article_info = Article.objects.get(pk=pk)
    delete = article_info.delete()
    return HttpResponse("Delete Success")
