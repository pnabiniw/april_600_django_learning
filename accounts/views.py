from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        pw = request.POST.get("password")
        if un and pw:
            user = authenticate(request=request, username=un, password=pw)
            if user:
                login(request, user)
                next_url = request.GET.get("next")
                if next_url:
                    return redirect(next_url)
                return redirect("crud_student")
        return redirect("user_login")
    return render(request, template_name="accounts/user_login.html")


def user_logout(request):
    logout(request)
    return redirect("root_page")