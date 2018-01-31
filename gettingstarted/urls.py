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
	#url(r'^getdata', hello.views.getdata, name='getdata'),
	#url(r'^contact', hello.views.contact, name='contact'),
	url(r'^logout1', hello.views.logout1, name='logout1'),
	url(r'^abc', hello.views.abc, name='abc'),
	#url(r'^verify', hello.views.verify, name='verify'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/$', hello.views.activate, name='activate'),
	url(r'^login1', hello.views.login1, name='login1'),
	url(r'^welcome', hello.views.welcome, name='welcome'),
	url(r'^hotel', hello.views.hotel, name='hotel'),
	url(r'^hotelservices', hello.views.hotelservices, name='hotelservices'),
	url(r'^backend/pricingplans', hello.views.pricingplans, name='pricingplans'),
	url(r'^onzeprijzen', hello.views.onzeprijzen, name='onzeprijzen'),
	url(r'^backend/admin', hello.views.admin, name='admin'), 
	url(r'^backend/adduser1', hello.views.adduser1, name='adduser1'), 
	url(r'^backend/hotelservices', hello.views.services, name='services'), 
	url(r'^backend/welcome', hello.views.home, name='home'), 
	url(r'^backend/getuser', hello.views.getuser, name='getuser'), 
	url(r'^backend/getemployee', hello.views.getemployee, name='getemployee'), 
	url(r'^backend/addemployee', hello.views.addemployee, name='addemployee'), 
	url(r'^backend/logoutadmin', hello.views.logoutadmin, name='logoutadmin'), 
	#url(r'^updateuserrecord', hello.views.updateuserrecord, name='updateuserrecord'),
	#url(r'^user_details/(?P<userid>\d+)/$', hello.views.user_details, name='user_details'),
	url(r'^deleteuser', hello.views.deleteuser, name='deleteuser'),
	url(r'^priceperweek', hello.views.priceperweek, name='priceperweek'),
	url(r'^deleteemployee', hello.views.deleteemployee, name='deleteemployee'),
	#url(r'^admin/', include(admin.site.urls)),
] 
