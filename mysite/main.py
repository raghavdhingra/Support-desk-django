from django.shortcuts import redirect
from django.contrib.auth.models import User

def home(request):
  user = request.user

  if user.is_authenticated:
    is_staff = User.objects.get(username=user).is_staff
    if is_staff:
      return redirect("/supportdesk/all-request")
    return redirect("/supportdesk/my-request")
  else:
    return redirect("/auth/login/")