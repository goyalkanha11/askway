from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated():
        user = request.user
        return HttpResponseRedirect(reverse('askway:home'))
    else:
        form = LoginForm()
        return render(request, 'askway/index.html', {'form': form})

def log(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('askway:home'))
            else :
                form = LoginForm()
                return render(request, 'askway/index.html',{'form':form, 'error_message':"Incorrect Credentials"})
    else:
        return HttpResponseRedirect(reverse('askway:index'))
def signup(request):
    if request.user.is_authenticated():
        user = request.user
        return HttpResponseRedirect(reverse('askway:home'))
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
                login(request, user)
                return HttpResponseRedirect(reverse('askway:home'))  
            else:
                return HttpResponse("<p>Please enter the same password in both of the password fields</p>")    
        else :
            return render(request, 'askway/signup.html', {'form': form})
    else:
        form = SignupForm()
        return render(request, 'askway/signup.html', {'form': form})

def home(request):
    if request.user.is_authenticated():
        user = request.user
        ques = Query.objects.all()
        return render(request, 'askway/home.html', {'ques': ques})
    else:
        return HttpResponse("<p>Please login to cotinue</p>")

def answer(request, question_id):
    if request.user.is_authenticated():
        if request.method =='POST':
            ques = get_object_or_404(Query, pk=question_id)
            ques.solution_set.create(answer = request.POST['answer'], answer_of = ques.question, answer_by = request.user)
        user = request.user
        ques = get_object_or_404(Query, pk=question_id)
        ans = ques.solution_set.all()
        form = AnsForm()
        if ans is not None:
            return render(request, 'askway/answer.html', {'ans': ans, 'form1':form, 'question_id':question_id})
        else:
            return HttpResponse("<p>Hello there is no answer posted yet</p>")
    else:
        form = LoginForm()
        return render(request, 'askway/index.html',{'form':form, 'error_message':"Incorrect Credentials"})
def post_ques(request): 
        if request.user.is_authenticated():
            user = request.user
            form = QuesForm()
            return render(request, 'askway/postques.html', {'form': form})


def post_question(request):
    if request.method == 'POST':
        form = QuesForm(request.POST)
        if form.is_valid():  
            f = form.save(commit=False)
            f.post_by = request.user
            f.save()
            return HttpResponseRedirect(reverse('askway:home'))

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('askway:log'))


        