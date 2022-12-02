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
    path('profil/', authentification.views.profil_page, name='profil'),
    path('profil_modify/<int:id>/', authentification.views.profil_modify_page, name='profil_modify'),
    path('profil_delete/<int:id>/', authentification.views.profil_delete, name='profil_delete'),
    path('flux/', litreview_app.views.home, name='flux'),
    path('ticket/', litreview_app.views.ticket, name='ticket'),


    path('ticket/<int:id>/', litreview_app.views.ticket_detail, name='ticket_modify'),
    path('review/<int:id>/', litreview_app.views.review_detail, name='review_modify'),

    path('ticket_delete/<int:id>/', litreview_app.views.ticket_delete, name='ticket_delete'),
    path('review_delete/<int:id>/', litreview_app.views.review_delete, name='review_delete'),
    
    path('review_without_ticket/', litreview_app.views.review_without_ticket, name='review_without_ticket'),
    path('review_with_ticket/<int:id>/', litreview_app.views.review_with_ticket, name='review_with_ticket'),
    path('subscription/', litreview_app.views.subscription, name='subscription'),
    path('subscription_unfollow/<int:id>/', litreview_app.views.subscription_unfollow, name='subscription_unfollow'),
    path('posts/', litreview_app.views.posts, name='posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
