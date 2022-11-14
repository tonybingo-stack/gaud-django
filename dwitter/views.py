from django.shortcuts import render
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token

def dashboard(request):
    return render(request, "dwitter/dashboard.html")


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

@requires_csrf_token
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
