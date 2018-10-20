from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddressForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import generic
from . import forms
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse
from .models import Profile
from PIL import Image
from django.core.files.base import ContentFile
import io


def load_user(backend, details, response, uid, user, *args, **kwargs):

    url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

    print(User)

    if url:
        r = requests.get(url)
        image_data = r.content
        user_profile = Profile(user=user)
        user_profile.image.save('{0}_social.jpg', ContentFile(image_data))


    return()