from django.conf.urls import url
from django_ses.views import handle_bounce
from django.views.decorators.csrf import csrf_exempt
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^notification/$',
        views.NotificationCreate.as_view(), name='NotificationCreate'),
    url(r'^loan_agreement/$',
        views.LoanAgreementCreate.as_view(), name='LoanAgreementCreate'),
    url(r'^ses/bounce/$', csrf_exempt(handle_bounce)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
