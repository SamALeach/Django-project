from django.shortcuts import render
from django.shortcuts import redirect
from .forms import UserAddForm
from .models import User
from django.template.loader import render_to_string
from django.http import HttpResponse
# Create your views here.


def user_add_view(request):
    form = UserAddForm(request.POST or None) #if there is post data it initializes it below if not its a GET
    context = {
        "form": form
    }
    if form.is_valid():
        user_object = form.save() #creates user

         #adds list of all users to context to fill home page and redirects there
        user_qset = User.objects.all()
        context["object_list"] = user_qset
        response = redirect('/', context=context)
        return response


    
    return render(request, "actions/add-view.html", context=context)
    

def user_edit_view(request, id=None):
    form = UserAddForm(request.POST or None) #if there is post data it initializes it below if not its a GET
    context = { #declares the context to be the passed form
        "form": form
    }
    if form.is_valid(): #checks to make sure form is valid before performing operations
        if 'edit_button' in request.POST: #conditonal trigger for if user chose edit
            new_fname = request.POST['first_name']
            new_lname = request.POST['last_name']
            new_email = request.POST['email']
            new_phonenum = request.POST['phone_num']
            new_role = request.POST['role']
            User.objects.filter(id=id).update(first_name=new_fname, last_name=new_lname, email=new_email, 
            phone_num=new_phonenum, role=new_role) #updates selected user with new data

            #adds list of all users to context to fill home page and redirects there
            user_qset = User.objects.all()
            context["object_list"] = user_qset
            response = redirect('/', context=context)
            return response
        elif 'delete_button' in request.POST:
            user_object = User.objects.get(id=id) #selects the user to delete
            user_object.delete() #deletes user

            #adds list of all users to context to fill home page and redirects there
            user_qset = User.objects.all()
            context["object_list"] = user_qset
            response = redirect('/', context=context)
            return response
    
        
    return render(request, "actions/edit-view.html", context=context)
