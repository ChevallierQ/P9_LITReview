from django.contrib import admin
from django.urls import path
import authentification.views
import litreview_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.LoginPage.as_view(), name='login'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('logout/', authentification.views.logout_page, name='logout'),
    path('flux/', litreview_app.views.home, name='flux'),
]
