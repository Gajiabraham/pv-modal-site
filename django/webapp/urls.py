from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login,name='login'),
    path('forgot-password', views.forgot_password,name='forget_password'),
    path('reset-password', views.reset_password,name='reset_password'),
    path('print-score-sheet', views.print_score,name='print_score'),
    path('add-student', views.add_student,name='add_student'),
    path('add-teacher', views.add_teacher,name='add_teacher'),
    path('auto-comment', views.auto_comment,name='auto_comment'),
    path('class', views.Class,name='Class'),
    path('dashboard1', views.dashboard1,name='dashboard1'),
    path('sessions', views.sessions,name='sessions'),
    path('stuent-details', views.student_details,name='student_details'),
    path('student', views.student,name='student'),
    path('subject', views.subject,name='subject'),
    path('teacher', views.teacher,name='teacher'),
    path('term', views.term,name='term'),
    path('users', views.users,name='users'),
    path('user1', views.user1,name='user1'),
    path('user2', views.user2,name='user2'),

    
   
]