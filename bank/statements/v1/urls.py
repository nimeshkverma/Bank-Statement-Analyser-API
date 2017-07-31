from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^bank/statement_analyser/$',
        views.StatementAnalyserDetails.as_view(), name='StatementAnalyserDetails'),
    url(r'^bank/statement_analyser_tool/$',
        views.StatementAnalyserToolDetails.as_view(), name='StatementAnalyserToolDetails'),
    url(r'^bank/statement_analyser_data_dump/$',
        views.StatementAnalyseDumperDetails.as_view(), name='StatementAnalyseDumperDetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
