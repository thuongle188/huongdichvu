from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, 'index.html')
def get_noti(request):
    return render(request,'noti.html')