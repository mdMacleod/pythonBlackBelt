from __future__ import unicode_literals
from django.db import models
from datetime import *
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        requiredFields = len(postData['firstName'])*len(postData["lastName"])*len(postData["email"])*len(postData["password"])*len(postData["confPass"])
        if requiredFields==0:
            errors['requiredFields'] = "You must fill out all fields"
        else:
            if len(postData['firstName']) < 2:
                errors['firstName'] = "First name should be at least three characters long"
            if len(postData['lastName']) < 2:
                errors['lastName'] = "Last name should be at least three characters long"
            
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):          
                errors['email'] = ("Invalid email address")
            if len(postData['password']) < 8:
                errors['passwordError'] = 'password must be at least 8 characters'
            if (postData['password']) != (postData['confPass']):
                errors['password'] = 'Passwords do not match'

        return errors

    def quote_validator(self, postData):
        errors = {}
        requiredFields = len(postData['name'])*len(postData['quote'])
        if requiredFields==0:
            errors['requiredFields'] = "you must fill out all fields"
        else:
            if len(postData['name']) < 2:
                errors['name'] = "Author's name should be atleast 2 characters"
            if len(postData['quote']) < 10:
                errors['quote'] = "Your quote should be atleast 10 characters long"
        return errors



class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Quote(models.Model):
    name = models.CharField(max_length=45)
    quote = models.TextField()
    submitted = models.ForeignKey(User, related_name = "userThatSubmitted")
    favorites = models.ManyToManyField(User, related_name="usersThatFavorite")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    objects = UserManager()