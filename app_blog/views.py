from django.shortcuts import render
from .models import Blog
# Create your views here.
def indexView(request):
    list_blogs = Blog.objects.all()

    context = {
        'list_blogs': list_blogs
    }
    print(context)
    return render(request, "blog/index.html", context)
def inboxView(request):
    return render(request, "blog/inbox.html")
def exploreView(request):
    return render(request, "blog/explore.html")
