from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='portal_landing'),
    path('add/', views.portal_add, name='portal_add'),
    path('list/', views.portal_list, name='portal_post'),
    path('edit/<int:id>/', views.portal_edit, name='portal_edit'),
    path('delete/<int:id>/', views.portal_delete, name='portal_delete')
]
