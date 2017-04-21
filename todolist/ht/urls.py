# -*- coding: utf-8 -*-
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ht import views


urlpatterns = [
	url(r'^home/$',views.HomeView.as_view()),
    url(r'^login/$',views.LoginView.as_view()),
   	url(r'^logout/$',views.Logout),
   	url(r'^register/$',views.RegisterView().as_view()),
   	url(r'^post/$',views.PostView.as_view()),
   	url(r'^list/$',views.ReturnTodoView.as_view()),
   	url(r'^change/$',views.ChangeView.as_view()),
   	url(r'^delete/$',views.DeleteView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)