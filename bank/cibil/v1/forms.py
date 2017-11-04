from django import forms


class CIBILReportDetailsForm(forms.Form):
    cibil_report_pdf = forms.FileField(label='CIBIL Report PDF')
