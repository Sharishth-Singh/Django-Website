from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Ice Creame lelo Admin"
admin.site.site_title = "Ice Creame lelo Admin Portal"
admin.site.index_title = "Welcome to Ice Creame lelo"

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
