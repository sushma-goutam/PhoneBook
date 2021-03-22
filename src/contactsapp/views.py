import logging
from logging.handlers import SysLogHandler

from django.shortcuts import render, redirect
from django.http import HttpResponse
import logzero  # https://logzero.readthedocs.io/en/latest/
from logzero import logger

from .models import Contact


# Setup rotating logfile with 3 rotations, each with a maximum filesize of 1MB:
# logzero.logfile("rotating-logfile.log", maxBytes=1e6, backupCount=3)

# Log to syslog,
logger = logging.getLogger('pblogger')

# def hello(request):
#    today = datetime.datetime.now().date()
#    return HttpResponse(today)

def index(request):
    contacts = Contact.objects.all()
    context = {"contacts": contacts}
    logger.info("Home Page")
    return render(request, 'contactsapp/index.html', context)


def create(request):
    contact = Contact(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                      phone_number=request.POST['phone_number'])
    contact.save()
    logger.info(f"New contact is created for {request.POST['first_name']}")
    return redirect('/')


def edit(request, id):
    contacts = Contact.objects.get(id=id)
    context = {'contacts': contacts}
    logger.info(f"Edit contact")
    return render(request, 'contactsapp/edit.html', context)


def update(request, id):
    contact = Contact.objects.get(id=id)
    contact.first_name = request.POST['first_name']
    contact.last_name = request.POST['last_name']
    contact.phone_number = request.POST['phone_number']

    contact.save()
    logger.info(f"Contact info is updated for {request.POST['first_name']}")
    return redirect('/')


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    logger.info("Contact deleted for id: {id}")
    return redirect('/')
