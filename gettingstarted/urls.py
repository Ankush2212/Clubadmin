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
	#url(r'^verify', hellao.views.verify, name='verify'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/$', hello.views.activate, name='activate'),
	url(r'^login1', hello.views.login1, name='login1'),
	url(r'^welcome', hello.views.welcome, name='welcome'),
	url(r'^eng', hello.views.en, name='en'),
	url(r'^en/holiday', hello.views.holiday, name='holiday'),
	url(r'^singleservice1', hello.views.singleservice1, name='singleservice1'),
	url(r'^en/pricing', hello.views.pricing, name='pricing'),
	url(r'^en/hotel', hello.views.hotel, name='hotel'),
	url(r'^help', hello.views.help, name='help'),
	url(r'^fullliteservice', hello.views.fullliteservice, name='fullliteservice'),
	url(r'^priceperweekenglish', hello.views.priceperweekenglish, name='priceperweekenglish'),
	url(r'^fullliteserviceenglish', hello.views.fullliteserviceenglish, name='fullliteserviceenglish'),
	url(r'^singleservicefordutch', hello.views.singleservicefordutch, name='singleservicefordutch'),
	url(r'^woningverhuur', hello.views.woningverhuur, name='woningverhuur'),
	url(r'^backend/pricingplans', hello.views.pricingplans, name='pricingplans'),
	url(r'^onzeprijzen', hello.views.onzeprijzen, name='onzeprijzen'),
	url(r'^backend/admin', hello.views.admin, name='admin'), 
	url(r'^backend/adduser1', hello.views.adduser1, name='adduser1'), 
	url(r'^backend/hotelservices', hello.views.services, name='services'), 
	url(r'^backend/welcome', hello.views.home, name='home'), 
	url(r'^backend/getuser', hello.views.getuser, name='getuser'), 
	url(r'^backend/hotels', hello.views.hotels, name='hotels'), 
	url(r'^backend/airbnb', hello.views.airbnb, name='airbnb'), 
	url(r'^backend/getsingleservices', hello.views.getsingleservices, name='getsingleservices'), 
	url(r'^backend/getemployee', hello.views.getemployee, name='getemployee'), 
	url(r'^backend/addemployee', hello.views.addemployee, name='addemployee'), 
	url(r'^backend/logoutadmin', hello.views.logoutadmin, name='logoutadmin'), 
	#url(r'^updateuserrecord', hello.views.updateuserrecord, name='updateuserrecord'),
	url(r'^backend/editsingleservice/(?P<userid>\d+)/$', hello.views.editsingleservice, name='editsingleservice'),
	url(r'^backend/editpricingplan/(?P<userid>\d+)/$', hello.views.editpricingplan, name='editpricingplan'),
	url(r'^updatesingleservice', hello.views.updatesingleservice, name='updatesingleservice'),
	url(r'^deletesingleservice', hello.views.deletesingleservice, name='deletesingleservice'),
	url(r'^updateprice', hello.views.updateprice, name='updateprice'),
	url(r'^deleteuser', hello.views.deleteuser, name='deleteuser'),
	url(r'^priceperweek', hello.views.priceperweek, name='priceperweek'),
	url(r'^deletepriceservice', hello.views.deletepriceservice, name='deletepriceservice'),
	url(r'^deleteemployee', hello.views.deleteemployee, name='deleteemployee'),
	#url(r'^admin/', include(admin.site.urls)),
] 
