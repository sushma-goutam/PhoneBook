from rest_framework import serializers

from contactsapp.models import Contact


class ContactsSerializer(serializers.ModelSerializer):
    # phone_number = serializers.CharField(required=False, allow_blank=True)
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ('first_name', 'last_name', 'phone_number')
