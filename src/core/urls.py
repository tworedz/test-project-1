from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

api_v1_urls = [
    path("employees/", include("employees.urls")),
    path("departments/", include("departments.urls")),
]

api_urls = [
    path("v1/", include((api_v1_urls, "v1"), namespace="v1")),
]

docs_urls = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]

admin_urls = [
    path("jet/", include("jet.urls", "jet")),
    path("admin/", admin.site.urls),
]

urlpatterns = [
    path("api/", include((api_urls, "api"), namespace="api")),
    path("", include(docs_urls)),
    path("", include(admin_urls)),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    urlpatterns += [path("silk/", include("silk.urls"))]
