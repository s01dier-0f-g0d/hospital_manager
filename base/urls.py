from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='register'),
    path('display/',views.display,name='display'),
    path('update/<int:key>/',views.update,name='update'),
    path('remove/<int:key>/',views.deletePatient,name='remove'),
]