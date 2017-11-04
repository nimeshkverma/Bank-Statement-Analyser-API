from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^cibil/report_analyser_tool/$',
        views.CIBILReportTool.as_view(), name='CIBILReportTool'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
