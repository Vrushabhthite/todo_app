from django.urls import path
from . import views
from . import forms

urlpatterns = [
    # AUTH
    path('login/', forms.login_view, name='login'),
    path('register/', forms.register_view, name='register'),
    path('logout/', forms.logout_view, name='logout'),

    # TODO
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('delete_task/<int:pk>/', views.delet_task, name='delete_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
]
