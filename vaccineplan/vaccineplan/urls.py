import django.conf
import django.conf.urls.static
import django.contrib.admin
import django.urls

urlpatterns = [
    django.urls.path("", django.urls.include("homepage.urls")),
    django.urls.path("auth/", django.urls.include("users.urls")),
    django.urls.path(
        "auth/",
        django.urls.include("django.contrib.auth.urls"),
    ),
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path("clinics/", django.urls.include("clinics.urls")),
    django.urls.path("vaccines/", django.urls.include("vaccines.urls")),
    django.urls.path(
        "vaccine_calendar/",
        django.urls.include("vaccine_calendar.urls"),
    ),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.STATIC_URL,
    document_root=django.conf.settings.STATIC_ROOT,
)
urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

if django.conf.settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include(debug_toolbar.urls),
        ),
    )
