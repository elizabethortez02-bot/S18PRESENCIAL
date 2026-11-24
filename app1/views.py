from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.utils.http import url_has_allowed_host_and_scheme


def inicio_view(request):
    return render(request, "inicio.html", {
        "usuario": request.user
    })


def registro_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = UserCreationForm()

    return render(request, "registro.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("inicio")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())

            next_url = request.POST.get("next") or request.GET.get("next")

            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}
            ):
                return redirect(next_url)

            return redirect("inicio")
    else:
        form = AuthenticationForm(request)

    return render(request, "login.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("inicio")


@login_required
def servicios_view(request):
    return render(request, "servicios.html")


@login_required
def perfil_view(request):
    return render(request, "perfil.html", {
        "usuario": request.user
    })