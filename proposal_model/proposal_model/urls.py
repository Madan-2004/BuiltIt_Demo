from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect the homepage to the upload page or admin dashboard
def home_redirect(request):
    return redirect('upload_proposal')

urlpatterns = [
    path('', home_redirect, name='home'),  # Redirect root URL to proposal upload
    path('admin/', admin.site.urls),
    path('', include('proposals.urls')),  # Includes proposal app URLs
    path('accounts/', include('django.contrib.auth.urls')), 
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.auth import views as auth_views

urlpatterns += [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

