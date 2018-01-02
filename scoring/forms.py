from django import forms


class SubmitForm(forms.Form):
    # required=False 要詢問!!!!
    Std_ID = forms.CharField(label='Please Enter Your Student ID', max_length=15, required=False)
    Json_Str = forms.CharField(label='Please Enter Your Json Result', max_length=1000, required=False)
