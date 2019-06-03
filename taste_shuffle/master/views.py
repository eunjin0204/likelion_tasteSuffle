from django.shortcuts import render,redirect
from user.models import room
# Create your views here.
def login(request):
    return render(request,'login.html')

def make(request):
    return render(request,'make.html')

def option(request):
    name = request.GET['master_name']
    return render(request,'option.html',{'name':name})

def create(request):
    myroom = room()
    myroom.title = request.GET['title']
    myroom.team_number = request.GET['team_number']
    myroom.per_team = request.GET['per_team']
    myroom.leader_name = 'test'
    myroom.category = request.GET['category']
    myroom.save()
    return redirect('/')

def destroy(request, room_id):
    return redirect('/')