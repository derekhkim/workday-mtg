from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from django_htmx.middleware import HtmxDetails

from .models import PlayerForm

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

@require_GET
def index(request: HtmxHttpRequest) -> HttpResponse:
    return render(request, "index.html")

@require_http_methods(["GET", "POST"])
def register(request: HtmxHttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    else: 
        form = PlayerForm()
    return render(request, "register.html", {'form': form})

# @require_GET
# def csrf_demo(request: HtmxHttpRequest) -> HttpResponse:
#     return render(request, "csrf-demo.html")


# @require_POST
# def csrf_demo_checker(request: HtmxHttpRequest) -> HttpResponse:
#     form = OddNumberForm(request.POST)
#     if form.is_valid():
#         number = form.cleaned_data["number"]
#         number_is_odd = number % 2 == 1
#     else:
#         number_is_odd = False
#     return render(
#         request,
#         "csrf-demo-checker.html",
#         {"form": form, "number_is_odd": number_is_odd},
#     )