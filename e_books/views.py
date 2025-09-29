from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout
from django.contrib import messages
from django.db import IntegrityError
from .models import Userregistration, Book
from .forms import User_registrationForm,User_loginForm, BookForm
from .email_utils import send_registration_email

def Usersignup(request):
    if request.method == 'POST':
        form = User_registrationForm(request.POST)
        if form.is_valid():
            try:
                data = form.save(commit=False)
                raw_password = form.cleaned_data.get('password')
                data.password = make_password(raw_password)   # hash password
                data.save()
                
                # Send real welcome email
                email_sent = send_registration_email(data.email, data.username)
                
                if email_sent:
                    messages.success(request, "Account created successfully! Welcome email sent to your inbox. 📧")
                else:
                    messages.success(request, "Account created successfully! (Email delivery failed)")
                
                return redirect('userlogin')
            except IntegrityError:
                form.add_error('email', "This email is already registered.")
            except Exception as e:
                form.add_error(None, f"Unexpected error: {str(e)}")
    else:
        form = User_registrationForm()

    return render(request, "usersignup.html", {'form': form})


def Userlogin(request):
    if request.method == 'POST':
        form = User_loginForm(request.POST)
        if form.is_valid():
            try:
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                user = Userregistration.objects.filter(email=email).first()
                if user and check_password(password, user.password):
                    request.session['user_id'] = user.id 
                    messages.success(request, "Login successful! 🎉")
                    return redirect('Userhome')
                else:
                    form.add_error(None, "Invalid email or password")
            except Exception as e:
                form.add_error(None, f"Something went wrong: {str(e)}")
    else:
        form = User_loginForm()
    
    return render(request, "userlogin.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('userlogin')    

def Userhome(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('userlogin')
    books = Book.objects.all()
    return render(request, "userhome.html", {"books": books})

 


def AddBook(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('userlogin')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user_id = user_id
            book.save()
            return redirect('Userhome')
    else:
        form = BookForm()
    return render(request, "addbook.html", {"form": form})


def Details(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('userlogin')
    books = Book.objects.filter(user_id=user_id)
    return render(request, "details.html", {"books": books})    

    


def Update(request,pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('userlogin')
    item=get_object_or_404(Book,pk=pk)
    if request.method =='POST':
        form=BookForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return  redirect('Userhome')
    else:
        form=BookForm(instance=item)
    return render(request,"update.html",{'form':form})



def Book_delete(request,pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('userlogin')
    item=get_object_or_404(Book,pk=pk)
    if request.method =='POST':
        item.delete()
        return redirect('Userhome')
    else:
        return render(request,"delete.html",{'item':item})
    