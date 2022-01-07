from django.shortcuts import render


def main_page(request):
    return render(request, 'mainapp/index.html')


def rules_site(request):
    return render(request, 'mainapp/rules.html')
