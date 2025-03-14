from django.conf import settings
from django.urls import path
from django.contrib import admin

from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path(r'^$', index),
    path(r'^health$', health),
    path(r'^admin/', admin.site.urls),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         url(r'^__debug__/', debug_toolbar.urls)),
#     ] + urlpatterns
