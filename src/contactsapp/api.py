from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas import AutoSchema

from .models import Contact
from .serializers import *

import coreapi


class ContactListSchema(AutoSchema):
    "This is needed for passing payload to requests made from swagger."
    def get_manual_fields(self, path, method):
        extra_fields = []
        if method.lower() in ['post', 'put']:
            extra_fields = [coreapi.Field('id'),
                            coreapi.Field('first_name'),
                            coreapi.Field('last_name'),
                            coreapi.Field('phone_number')
                            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_fields


class UserAuthentication(ObtainAuthToken):
    schema = ContactListSchema()

    def post(self, request, *args, **kwargs):
        serializer= self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class ContactList(APIView):
    schema = ContactListSchema()

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
    schema = ContactListSchema()

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
