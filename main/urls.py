from .views import main,search_view,order_event,login_user,logout_view,my_orders,delete_my_order,register_user
from django.urls import path

urlpatterns = [
    path('',main,name="home"),
    path('login/',login_user,name="login"),
    path('register/',register_user,name="register"),
    path('logout/',logout_view,name="logout"),
    path('my-orders/',my_orders,name="orders"),
    path('delete-order/<int:id>/',delete_my_order,name="deleteOrder"),
    path('search-list/',search_view,name="search_view"),
    path('createOrder/',order_event,name="createOrder")
]