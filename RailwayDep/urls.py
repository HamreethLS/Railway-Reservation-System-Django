from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("admin_homepage/", views.admin_homepage, name="admin_homepage"),
    path("user_login/", views.user_login, name="user_login"),
    path("book_ticket/<int:train_id>/", views.booking, name="booking"),
    path("train_list/", views.train_list, name="trains_list"),
    path("train_schedule/<int:train_id>/", views.train_schedule, name="train_schedule"),
    path("add_schedule/", views.add_schedule, name="add_schedule"),
    path("register/", views.register, name="register"),
    path("password_reset/",views.password_reset,name="password_reset"),
    path('user_dashboard/',views.user_dashboard,name="user_dashboard"),
    path('view_ticket/',views.view_ticket,name="view_ticket"),
    path('logout/',views.logout,name="logout"),
    path('add_station/', views.add_station, name='add_station'),
    path('add_train/', views.add_train, name='add_train'),   
]
