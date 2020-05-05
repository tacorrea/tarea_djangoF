from django.urls import path
from .views import HamburguesaAPIView, HamburguesaDetails, GenericAPIView, IngredienteAPIView, IngredienteDetails, HamburguesaIngrediente

urlpatterns = [
    path('hamburguesa', HamburguesaAPIView.as_view()),
    path('hamburguesa/<int:id>', HamburguesaDetails.as_view()),
    path('ingrediente', IngredienteAPIView.as_view()),
    path('ingrediente/<int:id>', IngredienteDetails.as_view()),

    path('generic/hamburguesa/<int:id>', GenericAPIView.as_view()),
    path('hamburguesa/<int:id>/ingrediente/<int:iid>', HamburguesaIngrediente.as_view()),
    #path('detail/<int:pk>/', article_detail)
]