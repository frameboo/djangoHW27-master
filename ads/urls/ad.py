from ads.views.ad import *
from django.urls import path

urlpatterns = [
    path('', AdListView.as_view()),
    path('<int:pk>/', AdDetailView.as_view()),
    path('<int:pk>/update/', AdUpdateView.as_view()),
    path('create/', AdCreateView.as_view()),
    path('<int:pk>/delete/', AdDeleteView.as_view()),
]
