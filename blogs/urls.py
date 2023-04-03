from django.urls import path

from blogs import views

urlpatterns = [
    path('', views.home_page),
    path('receta/<slug>', views.PostDetailView.as_view(), name='post'),
]
