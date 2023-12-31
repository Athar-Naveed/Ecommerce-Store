from django.urls import path
from . import views

app_name = 'item'
urlpatterns = [
    path('',views.browse_item,name="browse_item"),
    path('new/',views.new,name="new"),
    path('<int:pk>',views.detail,name="detail"),
    path('<int:pk>/delete/',views.delete_item,name='delete_item'),
    path('<int:pk>/edit/',views.edit_item,name='edit_item'),
]
