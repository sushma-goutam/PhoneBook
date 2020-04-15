# Using Swagger with Django

### Include new project dependency

##### Note: 'django-rest-swagger' is not maintained anymore. Update it to use newer alternative.
(They suggest switching to drf-yasg )

Add 'django-rest-swagger' to 'requirements.txt' file 

### Install it in python development environment
``` 
pip install django-rest-swagger
``` 
### Update 'settings.py'

Modify installed app list and Rest Framework config in 'settings.py'
``` 
INSTALLED_APPS = [
    ....
    'rest_framework',
    'rest_framework_swagger',
]

REST_FRAMEWORK = {
    ......
    # This is needed to fix ''AutoSchema' object has no attribute 'get_link' ” error' in Swagger
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
``` 

### Add a path to test swagger UI

Modify main project's urls.py and add the below lines
``` 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="PhoneBook")

urlpatterns = [
    ......
    url(r'^api/$', schema_view),
]
``` 

### Modify obsolete entry in rest-framework-swagger template
```
Open '\env\Lib\site-packages\rest_framework_swagger\templates\rest_framework_swagger\index.html'
In line 2, replace 
'{% load staticfiles %}' with 
{% load static %}
```

### Test Swagger UI

Start server, open web browser, login if needed and navigate to 'http://127.0.0.1:8000/api/'

### Sending a payload along with the request

Update the view where Rest APIs are defined (api.py)

```
.....
from .serializers import *
from rest_framework.schemas import AutoSchema
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
```

Now add the above schema to every view class which implements 'post' or 'put' method
```
class ContactList(APIView):
    schema = ContactListSchema()
    ......

    def post(self, request):
        serializer = ContactsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Use swagger session login 

We can use swagger session login to try out the APIs without having to deal with the enforced authentication.

```
urlpatterns = [
    ......
    url(r'^api/$', schema_view),
    path('accounts/', include('rest_framework.urls')),  # Swagger login
]
``` 