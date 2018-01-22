from django.conf.urls import include, url
from django.conf import settings
from django.urls import path
from django.contrib import admin

admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
	path('admin/', admin.site.urls),
	url(r'^$', hello.views.index, name='index'),
	#url(r'^addadmindetails', hello.views.addadmindetails, name='addadmindetails'),
	url(r'^getdata', hello.views.getdata, name='getdata'),
	#url(r'^contact', hello.views.contact, name='contact'),
	url(r'^logout1', hello.views.logout1, name='logout1'),
	url(r'^login1', hello.views.login1, name='login1'),
	url(r'^welcome', hello.views.welcome, name='welcome'),
	url(r'^backend/admin', hello.views.admin, name='admin'), 
	url(r'^backend/adduser1', hello.views.adduser1, name='adduser1'), 
	url(r'^backend/hotelservices', hello.views.services, name='services'), 
	url(r'^backend/welcome', hello.views.home, name='home'), 
	url(r'^backend/logoutadmin', hello.views.logoutadmin, name='logoutadmin'), 
	url(r'^updateuserrecord', hello.views.updateuserrecord, name='updateuserrecord'),
	url(r'^user_details/(?P<userid>\d+)/$', hello.views.user_details, name='user_details'),
	url(r'^deleteuser/(?P<userid>\d+)/$', hello.views.deleteuser, name='deleteuser'),
	#url(r'^admin/', include(admin.site.urls)),
] 
