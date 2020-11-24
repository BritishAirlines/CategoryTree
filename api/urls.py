from django.urls import path
from .views import CategoriesView

urlpatterns = [
     path('categories/', CategoriesView.as_view()),
     path('categories/<int:pk>/', CategoriesView.as_view()),
]
