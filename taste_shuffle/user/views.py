from django.shortcuts import render,redirect,get_object_or_404
from .models import room, user_choice
from django.core.paginator import Paginator

# Create your views here.
def rooms(request):
    rooms=room.objects
    room_list=room.objects.all()
    return render(request,'rooms.html',{'room_list':room_list})

def roomDetail(request, room_id):
    detail = get_object_or_404(room,pk=room_id)
    food_img_list = ['food/동남아식.jpg','food/양식.jpg','food/일식.jpg','food/중식.jpg','food/한식.jpg']
    music_img_list =['music/댄스.jpg','music/발라드.jpg','music/클래식.jpg','music/팝송.jpg','music/힙합.jpg']
    movie_img_list = ['movie/공포영화.jpg','movie/로맨스.jpg','movie/코미디.jpg','movie/판타지.jpg','movie/히어로물.jpg']
    trip_img_list = ['trip/아메리카.jpg','trip/아시아.jpg','trip/아프리카.jpg','trip/오세아니아.jpg','trip/유럽.jpg']
    img_list = [food_img_list,music_img_list,movie_img_list,trip_img_list]
    return render(request, 'roomDetail.html', {'roomDetail' : detail,'img_list':img_list})

def result(request, room_id):
    user = user_choice()
    user.user_name=request.GET['username']
    user.user_select=request.GET['test']
    user.user_roomnum = room_id
    user.save()
    category=request.GET['category']
    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []

    users=user_choice.objects.all()
    
    for one in users:
        if one.user_roomnum == room_id:
            if one.user_select == 1:
                group1.append(one.user_name)
            elif one.user_select == 2:
                group2.append(one.user_name)
            elif one.user_select == 3:
                group3.append(one.user_name)
            elif one.user_select == 4:
                group4.append(one.user_name)
            else:
                group5.append(one.user_name)

    return render(request,'result.html', {'group1':group1, 'group2':group2,'group3':group3,'group4':group4, 'group5':group5,'category':category})

def main(request):
    return render(request,'main.html')

