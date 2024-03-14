from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        room_number=request.POST.get('room_number')
    return render(request,'index1.html')
