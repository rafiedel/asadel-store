from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245485',
        'name': 'Rafie Asadel Tarigan',
        'pbp_class': 'F'
    }

    return render(request, "main.html", context)