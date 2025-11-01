from django.urls import path

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='register'),
    path('display/',views.display,name='display'),
    path('update/<int:key>/',views.update,name='update'),
    path('remove/<int:key>/',views.deletePatient,name='remove'),


    path('create_disease/',views.create_disease,name='create_disease'),
    path('read_disease/',views.read_disease,name='read_disease'),
    path('update_disease/<int:key>/',views.update_disease,name='update_disease'),
    path('delete_disease/<int:key>/',views.delete_disease,name='delete_disease'),
    path('history/',views.history,name='history'),
    path('restore/<int:key>/',views.restore,name='restore'),
]