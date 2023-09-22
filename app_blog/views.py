from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, "blog/index.html")
def inboxView(request):
    return render(request, "blog/inbox.html")
def exploreView(request):
    return render(request,"blog/explore.html")
