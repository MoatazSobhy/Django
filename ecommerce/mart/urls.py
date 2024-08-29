# from django.urls import path , include
# from . import views
# # from django.contrib import admin


# # urlpatterns = [
# #    path('',views.index, name='index'),
# #    path('/show',views.show, name='show')
# # ]

# # urls.py
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('',views.index, name='index'),
#     path('/show',views.show, name='show')
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),  # Fixed the path to not start with '/'
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
