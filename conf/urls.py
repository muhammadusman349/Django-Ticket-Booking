from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse
from conf.views import IndexView
from rest_framework.authtoken.views import obtain_auth_token
import os


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include('booking.urls')),

    # Health check endpoint
    path('health/', lambda r: HttpResponse('OK')),

    # Add other paths that should be excluded from SPA catch-all
] + static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))

# Catch-all pattern should be last
urlpatterns += [
    # Exclude common paths from SPA routing
    re_path(r'^(?!static|media|admin|api|health).*$', IndexView.as_view(), name='index'),
]
