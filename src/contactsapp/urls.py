from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit/update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
