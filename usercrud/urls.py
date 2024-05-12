from django.urls import path
from usercrud.views import UserView

urlpatterns = [
    path("app/",view=UserView.as_view()),

]