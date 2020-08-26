from django.shortcuts import render, redirect, get_object_or_404

def home_page(request):
    return render(request, "core/index.html")
