from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard1')  # Redirect to admin dashboard page
        else:
            error_message = "Invalid credentials or not an admin user."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')




def dashboard1(request):
    return render(request, 'dashboard1.html')



def forgot_password(request):
    return render(request, 'forgot-password.html')




def reset_password(request):
    return render(request, 'reset-password.html')




def print_score(request):
    return render(request, 'print-score-sheet.html')





def add_student(request):
    return render(request, 'add-student.html')





def add_teacher(request):
    return render(request, 'add-teacher.html')




def auto_comment(request):
    return render(request, 'auto-comment.html')



def Class(request):
    return render(request, 'class.html')





def sessions(request):
    return render(request, 'sessions.html')



def student_details(request):
    return render(request, 'student-details.html')



def student(request):
    return render(request, 'student.html')



def subject(request):
    return render(request, 'subject.html')



def teacher(request):
    return render(request, 'teacher.html')



def term(request):
    return render(request, 'term.html')



def users(request):
    return render(request, 'users.html')



def user1(request):
    return render(request, 'users1.html')


def user2(request):
    return render(request, 'users2.html')