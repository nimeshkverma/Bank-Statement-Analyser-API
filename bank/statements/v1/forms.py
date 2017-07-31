from django import forms


class StatementAnalyserToolForm(forms.Form):
    threshold = forms.IntegerField(label='Threshold Amount')
    bank_statements_pdf = forms.FileField(label='Bank Statement PDF')
    bank_statements_pdf_password = forms.CharField(widget=forms.PasswordInput(),
                                                   label="Bank Statement PDF's password",
                                                   required=False,
                                                   max_length=50)
