# swagger.py
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="vrms",
        default_version='v1',
        description="API for vrms",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path('swagger<format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
