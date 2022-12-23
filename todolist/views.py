import datetime
from django.shortcuts import render
from todolist.models import Tasks
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from todolist.forms import TaskForm
from django.urls import reverse

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login first
            response = HttpResponseRedirect(reverse("todolist:show_todos")) # create response
            response.set_cookie('username', username)
            response.set_cookie('last_login', str(datetime.datetime.now())) # create last_login cookie and add it to response
            return response
        else:
            messages.info(request, 'Wrong Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login_user'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/') # login first before doing this
def show_todos(request):
    # filters the user, so that each user can have their own todolist
    data = Tasks.objects.filter(user = request.user)
    context = {
        # using cookies since it is a rememberable temporary data
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
        'todos': data,

    }
    return render(
        request,
        'todolist.html',
        context
    )

@login_required(login_url='/todolist/login/') # login first before doing this
def new(request):
    # filters the user, so that each user can have their own todolist
    data = Tasks.objects.filter(user = request.user)
    context = {
        # using cookies since it is a rememberable temporary data
        'username': request.COOKIES['username'],
        'last_login': request.COOKIES['last_login'],
        'todos': data,

    }
    return render(
        request,
        'newtodolist.html',
        context
    )

@login_required(login_url='/todolist/login/') # login first before doing this
def new_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form_check = form.save(commit=False)
            form_check.user = request.user
            form_check.save()
            return HttpResponseRedirect(reverse('todolist:show_todos'))
        else:
            messages.info(request, "There's a problem with the data, please try again")
    
    # when requesting 
    return render(request, 'new_task.html', {'form': form})
            

    ...

@login_required(login_url='/todolist/login/') # login first before doing this
def refresh(request, id):
    task = Tasks.objects.get(user = request.user, pk = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todos')
    ...

@login_required(login_url='/todolist/login/') # login first before doing this
def delete(request, id):
    task = Tasks.objects.get(user = request.user, pk = id)
    task.delete()
    return redirect('todolist:show_todos')
