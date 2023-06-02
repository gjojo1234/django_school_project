from django.urls import path
from . import views

urlpatterns = [
    path('hello_world', views.hello_world, name="hello_world"),
    path('school', views.school, name="school"),
    path('subject', views.subject_link, name="subject"),
    path('subject/<int:pk>', views.subject_detail, name="subject_detail"),
    path('teacher', views.teacher, name="teacher"),
    path('teacher/<int:pk>', views.teacher_detail, name="teacher_detail")
]