from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
import bcrypt
from django.db.models import Count

from .models import *



# //NOTE LOGIN HOME
def index(request):


    return render(request, "beltApp/login.html")


def success(request):

    context = {
        'user' : User.objects.get(id=request.session['userid']),
    }

    return render(request, 'beltApp/success.html', context)

# //NOTE PET DASHBOARD
def dashboard(request):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['userid']),
        'quote' : Quote.objects.all(),
        
    }

    return render(request, 'beltApp/dashboard.html', context)



# //NOTE USER PAGE 

def user(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    context = {
        'user' : User.objects.get(id=id),
        'usersubmitted' : Quote.objects.filter(submitted=User.objects.get(id=id))
    }

    return render(request, 'beltApp/user.html', context)

def edit(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/') 


    context = {
        'quote' : Quote.objects.get(id=id)
    }

    return render(request, 'beltApp/edit.html', context)


def editredirect(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    errors = User.objects.quote_validator(request.POST)
    if len(errors) > 0:
        print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+id)


    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=id)

    if user.id == quote.submitted.id: 
        quote = Quote.objects.get(id=id)
        quote.name=request.POST["name"]
        quote.quote=request.POST['quote']
        quote.save()

    else:
        messages.error(request, "You can't edit someone else's pet ya Cheater!")

    return redirect('/dashboard')


def delete(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=id)

    if user.id == quote.submitted.id: 

        deletequote = Quote.objects.get(id=id)
        deletequote.delete()

        return redirect('/dashboard')
    
    else:
        messages.error(request, "You can't delete someone else's pet ya Cheater!")
        return redirect('/dashboard')






    # //NOTE REGISTRATION REDIRECT
def register(request):

    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    
    else:

        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print(pw_hash)

        user = User.objects.create (
            firstName=request.POST['firstName'],
            lastName=request.POST['lastName'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['userid'] = user.id

    return redirect('/success')

# //NOTE LOGIN REDIRECT
def login(request):

    user = User.objects.filter(email=request.POST['email'])
    if user:
        loggedUser = user[0]

        if bcrypt.checkpw(request.POST['password'].encode(), loggedUser.password.encode()):
            request.session['userid'] = loggedUser.id
            return redirect('/success')
        
    messages.error(request, "Login or Password is incorrect")

    return redirect('/')

    # //NOTE DELETE ITEM
def delete(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=id)

    if user.id ==  quote.submitted.id: 

        deleteQuote = Quote.objects.get(id=id)
        deleteQuote.delete()

        return redirect('/dashboard')
    
    else:
        messages.error(request, "You can't delete someone else's pet ya Cheater!")
        return redirect('/dashboard')


    #  //NOTE LOGOUT THEN REDIRECT
def logout(request):

    request.session.flush()

    return redirect('/')

def newquote(request):

    errors = User.objects.quote_validator(request.POST)
    if len(errors) > 0:
        print(errors)
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/dashboard')

    user = User.objects.get(id=request.session['userid'])
    Quote.objects.create(name=request.POST['name'],
    quote=request.POST['quote'],
    submitted=user
    )

    return redirect('/dashboard')


def addfavorite(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=id)
    quote.favorites.add(user)

    return redirect('/dashboard')

def removefavorite(request, id):

    if 'userid' not in request.session:
        messages.error(request, "You have to log in!")
        return redirect('/')

    user = User.objects.get(id=request.session['userid'])
    quote = Quote.objects.get(id=id)
    quote.favorites.remove(user)

    return redirect('/dashboard')