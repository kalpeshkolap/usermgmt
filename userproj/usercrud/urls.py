from django.urls import path
from usercrud.views import UserView,UseridView

urlpatterns = [
    path("app/",view=UserView.as_view()),
    path("app/<str:id>",view=UseridView.as_view()),
]