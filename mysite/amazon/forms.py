from django import forms


class UserForm_login(forms.Form):
    username = forms.CharField(label="username", max_length=100)
    password = forms.CharField(label="password", widget=forms.PasswordInput)

class ProductForm(forms.Form):
    order_num = forms.IntegerField(label="quantity")
    x = forms.IntegerField(label="address_x")
    y = forms.IntegerField(label="address_y")
    ups_act = forms.IntegerField(label="UPS Account number", required=False)

class SearchForm(forms.Form):
    catalog = forms.CharField(label="search for catalog", required=False)
    name = forms.CharField(label="search for product name", required=False)