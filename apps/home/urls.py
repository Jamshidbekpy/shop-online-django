from django.urls import path
from .views import HomePageView, MyAccountPageView

urlpatterns = [
    path('', HomePageView.as_view()),
    path('my-account/', MyAccountPageView.as_view()),
]