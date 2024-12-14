from django.shortcuts import render
from datetime import datetime
import random

calculation_history = []

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

def expression_page(request):
    num_terms = random.randint(2, 4)
    terms = [random.randint(10, 99) for _ in range(num_terms)]

    operators = [random.choice(['+', '-']) for _ in range(num_terms - 1)]
    expression = ""
    result = terms[0]

    for i in range(num_terms):
        expression += str(terms[i])
        if i < num_terms - 1:
            expression += " " + operators[i] + " "
            if operators[i] == '+':
                result += terms[i + 1]
            else:
                result -= terms[i + 1]

    calculation_history.append({"expression": expression + " = " + str(result), "result": result})

    context = {
        "expression": expression + " = " + str(result)
    }
    return render(request, "expression.html", context)

def history_page(request):
    context = {
        "history": calculation_history
    }
    return render(request, "history.html", context)