from django.contrib import admin
from django.urls import path, include
from markdownblog.urls import router as blog_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(blog_router.urls)),
    path('markdownx/', include('markdownx.urls')),
]
