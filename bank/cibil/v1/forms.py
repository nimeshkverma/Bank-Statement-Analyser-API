from django import forms


class CIBILReportDetailsForm(forms.Form):
    customer_id = forms.IntegerField(label='Customer Id')
    cibil_report_pdf = forms.FileField(label='CIBIL Report PDF')
