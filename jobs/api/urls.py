from django.urls import path
from jobs.api.views import JobOfferCreateAPIView, JobOfferDetailAPIView

urlpatterns = [
    path('jobs/', JobOfferCreateAPIView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>/', JobOfferDetailAPIView.as_view(), name='jobs-detail'),
]