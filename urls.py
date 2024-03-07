from django.contrib import admin
from django.urls import path
from app import views
from .views import map_view,student
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path("login",views.login_page,name='login'),
    path("",views.index,name='home'),
    path("home",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("register",views.register,name='register'),
    path("logout",views.logout_page,name='logout_page'),
    # path("materialin",views.materialin,name='materailin'),
    # path("materialout",views.materialout,name='materialout'),
    path("teacher",views.teacher,name='teacher'),
    path("stats",views.stats,name='stats'),
    path("my_map",views.map_view,name='my_map'),
    path("student",views.student,name='student'),
    path("attendance",views.attendance,name='attendance')
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root = settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()