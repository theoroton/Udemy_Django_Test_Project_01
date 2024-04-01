from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    return render(request, "blog/article.html", context={
        "numero_article": numero_article,
    })
