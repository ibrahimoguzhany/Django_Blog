from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib import messages

# Create your views here.

def index(request):

    context = {
        "number1":10,
        "number2":20
    }

    return render(request, "index.html", context) 

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale basariyla olusturuldu.")
        return redirect("index")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article, id = id)
    return render(request, "detail.html", {"article":article})


def updateArticle(request, id):

    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance = article)

    if form.is_valid():
        
        article = form.save(commit=False)

        article.author = request.user
        article.save()

        messages.success(request, "Makale basariyla guncellendi.")
        return redirect("index")

    return render(request,"update.html",{"form": form})




