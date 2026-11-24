from datetime import datetime, date
from django.shortcuts import render

# Create your views here.
def index(request):
    today = date.today()
    return render(request, "newyear/index.html", {
        "newyear": today.month == 1 and today.day == 1
    })
