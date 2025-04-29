from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #CRUD
    path('display/', views.display_all, name='dis'),
    path('add/', views.add_record, name='add'),
    path('update/<int:id>', views.update_view, name='update'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    
]
