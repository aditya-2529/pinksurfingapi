from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/', views.add),
    # path('delete/',views.delete),
    # path('register/',views.registerUser)
]