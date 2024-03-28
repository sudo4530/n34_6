from django.urls import path
from .views import LandingPageView, CourseListView, TEacherListView

urlpatterns = [
    path("", LandingPageView.as_view(), name="landing"),
    path("courses/", CourseListView.as_view(), name="courses"),
    path("teachers/", TEacherListView.as_view(), name="teachers"),

]