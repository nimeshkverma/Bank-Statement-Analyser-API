from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^customer/send_otp/$', views.OtpCreate.as_view(),
        name='send_otp'),
    url(r'^admin/communications/transactional_sms/$', views.TransactionalSMS.as_view(),
        name='send_transactional_sms'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
