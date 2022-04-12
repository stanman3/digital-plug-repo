from django.urls import path
from digital_plug.web.views import show_index, logged_index, show_profile, register_profile, edit_creator, \
    edit_explorer, delete_creator, delete_explorer, show_project, upload_project, edit_project, delete_project, contact, \
    login, about

urlpatterns = (
    path('', show_index, name='show index'),
    path('home/', logged_index, name='logged index'),

    path('profile/', show_profile, name='show profile'),
    path('profile/register', register_profile, name='register profile'),
    path('profile/edit-creator/', edit_creator, name='edit creator'),
    path('profile/edit-explorer/', edit_explorer, name='edit explorer'),
    path('profile/delete-creator/', delete_creator, name='delete creator'),
    path('profile/delete-explorer/', delete_explorer, name='delete explorer'),

    path('project/', show_project, name='show project'),
    path('project/upload/', upload_project, name='upload project'),
    path('project/edit/<int:pk>/', edit_project, name='edit project'),
    path('project/delete/<int:pk>/', delete_project, name='delete project'),

    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
)
