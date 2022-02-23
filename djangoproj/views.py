# First web page rendered
from django.http import HttpResponse
from django.template.loader import render_to_string
from Users.models import User #import user models
from django.shortcuts import render

#route to home page that lists users
def home_view(request, id=None, *args, **kwargs):
    
    #gets list of users and size for display 
    user_qset = User.objects.all()
    qset_size = User.objects.count()
    
    context = {
        "object_list": user_qset,
        "qsize": qset_size,
    }
    for x in user_qset: #loop to hide the role tag for non Admins
        if x.role == "Admin":
            continue
        else:
            x.role = " " 
    String = render_to_string("home-view.html", context=context)
    return HttpResponse(String)