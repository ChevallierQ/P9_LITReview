from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentification.views
import litreview_app.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentification.views.LoginPage.as_view(), name='login'),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('logout/', authentification.views.logout_page, name='logout'),
    path('flux/', litreview_app.views.home, name='flux'),
    path('ticket/', litreview_app.views.ticket, name='ticket'),
    path('review_without_ticket/', litreview_app.views.review_without_ticket, name='review_without_ticket'),
    path('subscription/', litreview_app.views.subscription, name='subscription'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
