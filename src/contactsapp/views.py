from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Contact


# def hello(request):
#    today = datetime.datetime.now().date()
#    return HttpResponse(today)


def index(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    return render(request, 'contactsapp/index.html', context)


def create(request):
    contact = Contact(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                      phone_number=request.POST['phone_number'])
    contact.save()
    return redirect('/')


def edit(request, id):
    contacts = Contact.objects.get(id=id)
    context = {'contacts': contacts}
    return render(request, 'contactsapp/edit.html', context)


def update(request, id):
    contact = Contact.objects.get(id=id)
    contact.first_name = request.POST['first_name']
    contact.last_name = request.POST['last_name']
    contact.phone_number = request.POST['phone_number']

    contact.save()
    return redirect('/')


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('/')
