from django.shortcuts import render

# Create your views here.
def bs(request):
    return render(request,'bootstrap_download.html')