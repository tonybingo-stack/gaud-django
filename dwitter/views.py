from django.shortcuts import render
from .models import Profile
from django.views.decorators.csrf import csrf_exempt

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from dwitter.models import ImageProcess
from dwitter.serializers import ImageSerializer
from rest_framework.decorators import api_view

from .service import generate_images

def dashboard(request):
    return render(request, "dwitter/dashboard.html")
# @csrf_exempt
def hello(request):
    return JsonResponse({'imageURL':"hello"}, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def imageAPI(request):
    if request.method == 'GET':
        image_serializer = ImageSerializer('imageURL', many=True)
        # return JsonResponse(image_serializer.data, safe=False)
        # print(request)
        imagen = './dwitter/static/images/input.png'
        generate_images(imagen)
        return JsonResponse({'imageURL':"/static/result.png"}, safe=False)

        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        print("ok")
        # tutorial_data = JSONParser().parse(request)
        # tutorial_serializer = TutorialSerializer(data=tutorial_data)
        # if tutorial_serializer.is_valid():
        #     tutorial_serializer.save()
        #     return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        # return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #     # count = Tutorial.objects.all().delete()
    #     # return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
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
