from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PILIHAN_PEMBAYARAN = (
    ('P', 'Paypal'),
    ('C', 'COD'),
)

class CheckoutForm(forms.Form):
    alamat_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Alamat Anda', 'class': 'textinput form-control'}))
    alamat_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartement, Rumah, atau yang lain (opsional)', 'class': 'textinput form-control'}))
    negara = CountryField(blank_label='(Pilih Negara)').formfield(widget=CountrySelectWidget(attrs={'class': 'countryselectwidget form-select'}))
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={'class': 'textinput form-outline', 'placeholder': 'Kode Pos'}))
    simpan_info_alamat = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    opsi_pembayaran = forms.ChoiceField(widget=forms.RadioSelect(), choices=PILIHAN_PEMBAYARAN)
    
class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'name', 'class': 'textinput form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'textinput form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'subject', 'class': 'textinput form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'message', 'class': 'textinput form-control'}))