from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('add/',views.Index,name='lalit'),
    path('delete/',views.delete,name='delete'),
    path('update/(?P<date>\w+)/',views.Update,name='update'),
    path('deleteall/',views.DeleteAll,name='deleteall')
]
