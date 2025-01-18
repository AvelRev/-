from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from first.views import my_page, time_page, calc_page, expression_page, history_page, delete_last_expression, clear_history, add_expression, str2words_page,logout_view,str_history

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_page/', my_page, name='my_page'),
    path('time/', time_page, name='time_page'),
    path('calc/', calc_page, name='calc_page'),
    path('expression/', expression_page, name='expression_page'),
    path('history/', history_page, name='history_page'),
    path('delete/', delete_last_expression, name='delete_last_expression'),
    path('clear/', clear_history, name='clear_history'),
    path('new/', add_expression, name='add_expression'),
    path('str2words/', str2words_page, name='str2words_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('str_history/', str_history, name='str_history'),

    path('', my_page),
]