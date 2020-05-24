"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from accounts.views import f_login,f_logout,f_register
from homepage.views import f_homepage
from blog.views import f_newblog,f_blog_sort,f_blog_category
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', f_homepage),
    url(r'^newblog/', f_newblog),

    url(r'^account/login/', f_login),
    url(r'^account/logout/', f_logout),
    url(r'^account/register/', f_register),

    url(r'^blog/(?P<id>[0-9]+)/', f_blog_sort),
    # url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile')
    url(r'^blog/(?P<category>[A-Za-z]+)/', f_blog_category),

    



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
