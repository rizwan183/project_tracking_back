from django.urls import path
from .views import ProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name='project'),
    path('<str:pk>', ProjectView.as_view(), name='project')
]
