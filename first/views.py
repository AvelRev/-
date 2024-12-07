from django.shortcuts import render
from datetime import datetime

def my_page(request):
    context = {
        "job": "Sigma",
        "city": "Moscow"
    }
    return render(request, "my_page.html", context)

def time_page(request):
    now = datetime.now()
    context = {
        "title": "Текущая дата и время",
        "date": now.strftime("%d.%m.%Y"),
        "time": now.strftime("%H:%M:%S")
    }
    return render(request, "time.html", context)


def calc_page(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)

    try:
        a = int(a)
    except ValueError:
        a = 0

    try:
        b = int(b)
    except ValueError:
        b = 0

    total = a + b

    context = {
        "a": a,
        "b": b,
        "total": total
    }

    return render(request, "calc.html", context)