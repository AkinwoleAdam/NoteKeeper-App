from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm,UpdateNoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db.models import Q
# Create your views here.

def register(request):
  form = UserCreationForm()
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      messages.success(request,'Your account has been successfully created!')
      return redirect('index')
  context = {'form':form}
  return render(request,'notesapp/register.html',context)

def loginUser(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
      login(request,user)
      messages.success(request,'You have successfully logged in!')
      return redirect('index')
    else:
      messages.error(request,'Username or Password is incorrect!')
  return render(request,'notesapp/login.html')

def logoutUser(request):
  logout(request)
  return redirect('login')

@login_required(login_url='login')
def index(request):
    notes = Note.objects.filter(user=request.user)
    q = request.GET.get('q')
    if q:
      notes = Note.objects.filter(Q(title__icontains=q) | Q(description__icontains=q)).filter(user=request.user)
    else:
      q = ''
      notes = Note.objects.filter(user=request.user)
    context = {'notes':notes}
    return render(request,'notesapp/index.html',context)
    
    
@login_required(login_url='login')
def new_note(request):
  form = NoteForm()
  if request.method=="POST":
    form=NoteForm(request.POST)
    if form.is_valid():
      form = form.save(commit=False)
      form.user = request.user
      form.save()
      return redirect("index")
  context = {'form':form}
  return render(request,'notesapp/new_note.html',context)
    
    
@login_required(login_url='login')
def update_note(request,pk):
  try:
    note = Note.objects.get(id=pk,user=request.user)
  except:
    return redirect('404')
  form=UpdateNoteForm(instance=note)
  context = {'form':form}
  if request.method=="POST":
    form=UpdateNoteForm(request.POST,instance=note)
    if form.is_valid():
      update = form.save(commit=False)
      update.user = request.user
      update.save()
      return redirect("index")
  return render(request,'notesapp/update_note.html',context)
 
    
@login_required(login_url='login')
def delete_note(request,pk):
  try:
    note = Note.objects.get(id=pk,user=request.user)
  except:
    return redirect('404')
  form=NoteForm(instance=note)
  context = {'form':form,'note':note}
  if request.method=="POST":
    note.delete()
    return redirect("index")
  return render(request,'notesapp/delete_note.html',context)             
 
 
@login_required(login_url='login')  
def notFound(request):
  return render(request,'notesapp/404.html')