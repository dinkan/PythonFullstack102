from django.shortcuts import render

from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hello world!")

from django.template import loader
""" 
def students(request):
  template = loader.get_template('welcome.html')
  return HttpResponse(template.render())
 """
from .models import Student
def students(request):
  studentlist = Student.objects.all().values()
  template = loader.get_template('studentslist.html')
  context = {
    'studentlist': studentlist,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Student.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'thisstudent': mymember,
  }
  return HttpResponse(template.render(context, request))

def update(request, id):
  mymember = Student.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'thisstudent': mymember,
  }
  return HttpResponse(template.render(context, request))

def updatesub(request, id):
  mymember = Student.objects.get(id=id)
  mymember.rollnumber=request.POST["rollnumber"]
  mymember.name=request.POST["name"]
  mymember.save()
  #return HttpResponse("Record updated")
  response = redirect('/students')
  return response  

def deletesub(request, id):
  mymember = Student.objects.get(id=id)
  #mymember.rollnumber=request.POST["rollnumber"]
  #mymember.name=request.POST["name"]
  mymember.delete()
  #return HttpResponse("Record updated")
  response = redirect('/students')
  return response  


def create(request):
  #mymember = Student.objects.get(id=id)
  template = loader.get_template('create.html')
  context = {
   
  }
  return HttpResponse(template.render(context, request))


def createsub(request):
  rollnumber=request.POST["rollnumber"]
  name=request.POST["name"]
  mymember = Student(rollnumber=rollnumber,name=name)
  mymember.save()
  response = redirect('/students')
  return response
  #return HttpResponse("Record Created")


  """ template = loader.get_template('detail.html')
  context = {
    'thisstudent': mymember,
  }
  return HttpResponse(template.render(context, request)) """