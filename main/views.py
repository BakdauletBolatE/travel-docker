from django.http.request import QueryDict
from django.shortcuts import get_object_or_404, redirect, render
from .models import Country, TravelCity,Gallery,TravelEvent,UserEvent
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
# Create your views here.


def main(request):
    galleries = Gallery.objects.all()
    travelEvents = TravelEvent.objects.all()
    country = Country.objects.all()

    data = {
        'galleries': galleries,
        'country':country,
        'travelEvents':travelEvents
    }
    return render(request,'main/index.html',data)

def singleView(request,pk):

    travelEvent = get_object_or_404(TravelEvent,id=pk)

    data = {
            "item": travelEvent
        }
    return render(request,'main/single.html',data)

def search_view(request):

    travelEvents = QueryDict()

    if request.method == 'POST':

        country_id = request.POST['country_id']
        date = request.POST['date']

        travelEvents = TravelEvent.objects.filter(travelCity__country__id=country_id,end_date__gt=date).all()
    
        data = {
            "travelEvents": travelEvents
        }
        return render(request,'main/search_list.html',data)
    
   
    
    return render(request,'main/search_list.html')


def login_user(request):

    if request.method == 'POST':

        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'auth/login.html')
            

    return render(request,'auth/login.html')

def register_user(request):

    if request.method == 'POST':

        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(name, email, password)
        print(user)
        user.save()
        user = authenticate(request,username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'auth/register.html')
            

    return render(request,'auth/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='/login/')
def order_event(request):

    if request.method == 'POST':

        travelEvent_id = request.POST['travelEvent_id']
        user_id = request.user.id

        exists = UserEvent.objects.filter(event_id=travelEvent_id,user_id=user_id)

        if len(exists) > 0:
            return redirect('orders')
    

        order = UserEvent.objects.create(
            user_id = user_id,
            event_id = travelEvent_id
        )

        order.save()

        print(order)

        return redirect('orders')


def delete_my_order(request,id):

    userEvent = UserEvent.objects.get(id=id)
    userEvent.delete()

    return redirect('orders')

def my_orders(request):

    user = request.user
    orders = user.orders.all()

    print(orders)

    data = {
        'orders': orders
    }

    return render(request,'main/orders.html',data)