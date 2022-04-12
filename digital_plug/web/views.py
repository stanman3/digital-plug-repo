from django.shortcuts import render


# Create your views here.
def show_index(request):
    return render(request, 'index.html')


def logged_index(request):
    return render(request, 'home.html')


def show_profile(request):
    return render(request, 'profile-creator.html')


def register_profile(request):
    return render(request, 'register.html')


def edit_creator(request):
    return render(request, 'edit-profile-creator.html')


def edit_explorer(request):
    return render(request, 'edit-profile-explorer.html')


def delete_creator(request):
    return render(request, 'delete-profile-creator.html')


def delete_explorer(request):
    return render(request, 'delete-profile-explorer.html')


def show_project(request):
    return render(request, 'single-post.html')


def upload_project(request):
    return render(request, 'upload-project.html')


def edit_project(request):
    return render(request, 'edit-project.html')


def delete_project(request):
    return render(request, 'delete-project.html')


def contact(request):
    return render(request, 'contact-creator.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')
