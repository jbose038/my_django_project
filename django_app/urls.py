"""django_app URL Configuration

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
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
import webPage.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', webPage.views.index, name='index'),
    path('signup/', webPage.views.signup, name='signup'),
    path('login/', webPage.views.login_, name='login'),
    path('home/', webPage.views.home, name='home'),
    path('logout/', webPage.views.logout_, name='logout'),
    path('home/newBlog/',webPage.views.createBlog, name='newBlog'),
    path('base/', webPage.views.base, name='base'),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('home/detail/<int:blog_id>/',webPage.views.detail, name='detail'),
    path('home/polls/', webPage.views.polls, name='polls'),
    path('home/polls/<int:question_id>/', webPage.views.poll_detail, name='poll_detail'),
    path('home/polls/<int:question_id>/results/', webPage.views.poll_result, name='poll_result'),
    path('home/polls/<int:question_id>/vote/',webPage.views.vote, name='vote'),
    path('home/newPoll/', webPage.views.createPoll, name='newPoll'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)