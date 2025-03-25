from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def change_img(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        profile = Profile(user=user)

        avatar = request.FILE.get('avatar')

        profile.avatar = avatar
        profile.save()
