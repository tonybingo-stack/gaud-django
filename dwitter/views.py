from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import base64
import os.path

from dwitter.models import ImageProcess
from dwitter.serializers import ImageSerializer

from .models import Profile
from .service import generatefromimage, generatefromtext

def dashboard(request):
    return render(request, "dwitter/dashboard.html")

@api_view(['GET', 'POST', 'DELETE'])
def imageAPI(request):
    
    if request.method == "POST":
        imageData = request.body
        ImageData = base64.b64decode(imageData)
        with open("dwitter/static/upload/input.png", "wb") as binary_file:
            # Write bytes to file
            binary_file.write(ImageData)

        imagen = './dwitter/static/upload/input.png'
        count = 0

        while(True):
            path = './dwitter/static/result/' + str(count) + '.png'
            isFile = os.path.exists(path)
            if isFile == True:
                count = count + 1
            else:
                break

        generatefromimage(imagen, count)
        return JsonResponse({"imageURL":'./static/result/' + str(count) + '.png'})

@api_view(['GET', 'POST', 'DELETE'])
def textAPI(request):
    
    if request.method == "POST":
        textData = request.body

        # print(textData)
        count = 0
        while(True):
            path = './dwitter/static/result/' + str(count) + '.png'
            isFile = os.path.exists(path)
            if isFile == True:
                count = count + 1
            else:
                break

        generatefromtext(textData, count)
        return JsonResponse({"imageURL":'./static/result/' + str(count) + '.png'})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
