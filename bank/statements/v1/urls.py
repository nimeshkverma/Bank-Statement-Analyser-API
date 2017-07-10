from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^bank/statement_analyser/$',
        views.StatementAnalyserDetails.as_view(), name='StatementAnalyserDetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
