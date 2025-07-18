from django.urls import path

from .views import WorkVolumeView

urlpatterns = [
    path('work-volume-list/', WorkVolumeView.as_view(), name='work-volume-list'),
]