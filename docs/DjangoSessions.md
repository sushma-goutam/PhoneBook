## Django Sessions – How to Create, Use and Delete Sessions
Read this [link](https://data-flair.training/blogs/django-sessions/)

HTTP is a stateless protocol, where every request made is always new to the server. 
The request on the server is always treated as if the user is visiting the site for the first time. 
This poses some problems like you can’t implement user login and authentication features. 

These problems were actually solved by Cookies.

### What are Cookies?

Cookies are small text files stored and maintained by the browser. 
It contains some information about the user and every time a request is made to the same server, 
the cookie is sent to the server so that the server can detect that the user has 
visited the site before or is a logged in user.

The cookies also have their drawbacks and a lot of times they become a path for the hackers and malicious websites 
to damage the target site.

### Drawbacks of Cookies

Since cookies store locally, the browser gives control to the user to accept or decline cookies. 
Many websites also provide a prompt to users regarding the same.

Cookies are plain text files, and those cookies which are not sent over HTTPS can be easily caught by attackers. 
Therefore, it can be dangerous for both the site and the user to store essential data in cookies and 
returning the same again and again in plain text.

After observing these problems of cookies, the web-developers came with a new and more secure concept, Sessions.

### What are Sessions?

The session is a semi-permanent and two-way communication between the server and the browser.

Let’s understand this technical definition in detail. 
Here semi means that session will exist until the user logs out or closes the browser. 
The two-way communication means that every time the browser/client makes a request, 
the server receives the request and cookies containing specific parameters and 
a unique Session ID which the server generates to identify the user. 

The Session ID doesn’t change for a particular session, but the website generates it every time a new session starts.

Generally, Important Session Cookies containing these Session IDs deletes when the session ends. 
But, this won’t have any effect on the cookies which have fix expire time.

### Django Sessions

Django considers the importance of sessions over the website and therefore provides you with middleware and 
inbuilt app which will help you generate these session IDs without much hassle.

django.contrib.sessions is an application which works on middleware.SessionMiddleware and is convenient to work.

The middleware.SessionMiddleware is responsible for generating your unique Session IDs. 
You will also require django.contrib.sessions application, if you want to store your sessions on the database.

When we migrate the application, we can see the django_session table in the database.

The django.contrib.sessions application is present in the list of INSTALLED_APPS in settings.py file.

For working on sessions, you will need to check whether your browser supports cookies or not.

Of course, you can go to the settings and quickly check that, but let’s make some view functions and URLs to understand 
the concepts in a better way. Ultimately, you will have to go to the browser settings if something went wrong.

### Checking Cookies on Browser

For adding view functions in our views.py file, enter:

Code:

    def cookie_session(request):
        request.session.set_test_cookie()
        return HttpResponse("<h1>dataflair</h1>")
    def cookie_delete(request):
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            response = HttpResponse("dataflair<br> cookie createed")
        else:
            response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
        return response
        
Now, add the urls to urlpatterns.

Code:

        path('testcookie/', cookie_session),
        path('deletecookie/', cookie_delete),
        
### Creating & Accessing Django Sessions

Django allows you to easily create session variables and manipulate them accordingly.

The request object in Django has a session attribute, which creates, access and edits the session variables. 
This attribute acts like a dictionary, i.e., you can define the session names as keys and their value as values.

* Step 1. We will start by editing our views.py file. Add this section of code.

Code:

    def create_session(request):
        request.session['name'] = 'username'
        request.session['password'] = 'password123'
        return HttpResponse("<h1>dataflair<br> the session is set</h1>")
    def access_session(request):
        response = "<h1>Welcome to Sessions of dataflair</h1><br>"
        if request.session.get('name'):
            response += "Name : {0} <br>".format(request.session.get('name'))
        if request.session.get('password'):
            response += "Password : {0} <br>".format(request.session.get('password'))
            return HttpResponse(response)
        else:
            return redirect('create/')

* Step 2. Add the urls in urlpatterns list.

Code:

        path('create/', create_session),
        path('access', access_session),

* Step 3. Now run this code:

1. search for access/       
2. search for access/ again

In the database, you will see the key and the data which has high encryption.

### Understanding the Code:

When you request for access/ URL without running the create/ request, you redirect to the create/ automatically 
if you have no cookie generated previously.

Now, when the create/ URL is sent, the SessionsMiddleware runs and generates a unique SessionID which is stored 
locally on the browser as a cookie for the user.

This cookie is now sent to the server every time alongside with the request and sessions. 
The application does the work of matching the SessionID with one in the database. 
It also stores some values and variables which we have created in the create_session() view function.     

The request object has a session attribute and when the server runs that code, the session middleware, and 
sessions application automatically works together.

request.session[] act as a python dictionary data-structure, and therefore, you can store the values 
alongside with their keys having meaningful names.

In the access_session() function, we have used get() alongside request.session and passed the value of the key.

Thus, you can access the sessions easily.    

### Deleting Django Sessions

After completing the sessions work, you can delete them quite easily.

Just include this view function inside views.py file.

Code:

    def delete_session(request):
        try:
            del request.session['name']
            del request.session['password']
        except for KeyError:
            pass
        return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")

Don’t worry if your cookie didn’t delete because we use this method only to delete your data in the Django database and 
not the session ID and cookie itself.

To delete the session related cookies completely, we use the flush() function, 
although sessions delete when the browser is closed.