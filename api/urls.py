from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mymodels', views.MyModelViewSet)

urlpatterns = [
    path('batch-destroy/', views.MyModelViewSet.batch_destroy, name='batch_destroy'),
    path('',views.getData),
    path('add/', views.add),
    path('delete/',views.delete),
    path('login/',views.getLogin)
]