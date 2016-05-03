from django.conf.urls import url
from . import views

# to make namespaces reference only this app (this way we can have 
# the same name in different apps)
app_name = 'users'

urlpatterns = [
    # /register/
    url(r'^register/$', views.UserRegisterFormView.as_view(), name='register'),

    # /login/
    url(r'^login/$', views.UserLogInFormView.as_view(), name='login'),

    # /logout/
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]