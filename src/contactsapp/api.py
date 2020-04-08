from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contact
from .serializers import *


class ContactList(APIView):
    def get(self, request):
        model = Contact.objects.all()
        serializer = ContactsSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(APIView):
    def get_contact(self, contact_id):
        try:
            model = Contact.objects.get(id=contact_id)
            return model
        except Contact.DoesNotExist:
            return

    def get(self, request, contact_id):
        if not self.get_contact(contact_id):
            return Response(f"Contact with id {contact_id} is not found", status=status.HTTP_404_NOT_FOUND)

        serializer = ContactsSerializer(self.get_contact(contact_id))
        return Response(serializer.data)

    def put(self, request, contact_id):
        if not self.get_contact(contact_id):
            return Response(f"Contact with id {contact_id} is not found", status=status.HTTP_404_NOT_FOUND)

        serializer = ContactsSerializer(self.get_contact(contact_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, contact_id):
        if not self.get_contact(contact_id):
            return Response(f"Contact with id {contact_id} is not found", status=status.HTTP_404_NOT_FOUND)

        model = self.get_contact(contact_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
