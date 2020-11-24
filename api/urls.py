from django.urls import path
from .views import CreateCategories, CategoryDetails


urlpatterns = [
     path('categories/', CreateCategories.as_view()),
     path('categories/<int:pk>/', CategoryDetails.as_view()),
]
