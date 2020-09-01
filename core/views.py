from django.shortcuts import render, redirect, get_object_or_404

def home_page(request):
    return render(request, "core/index.html")


def about_detail(request):
    return render (request, "core/about_detail.html")


def contact_detail(request):
    return render (request, "core/contact_detail.html")


def portfolio_detail(request):
    return render (request, "core/protfolio_detail.html")


def service_detail(request):
    return render (request, "core/service_detail.html")