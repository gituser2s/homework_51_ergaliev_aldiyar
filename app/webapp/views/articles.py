from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

db = []


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'cat_create.html')
    db.append(request.POST.get('cat_name'))
    print(request.POST)
    context = {
        'db': db,
        'age': 40,
        'mood': 10,
        'satiety': 40,
    }
    return render(request, 'cat.html', context=context)


