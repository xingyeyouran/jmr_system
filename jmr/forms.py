from django import forms


class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=40)
    user_password = forms.CharField(max_length=40, label='密码', widget=forms.PasswordInput)
