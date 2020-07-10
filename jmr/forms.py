from django import forms

from jmr.models import Resume


class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=40)
    user_password = forms.CharField(max_length=40, label='密码', widget=forms.PasswordInput)


class ResumeForm(forms.Form):
    seeker_name = forms.CharField(label='姓名', max_length=20)
    seeker_race = forms.CharField(label='民族', max_length=4)
    seeker_gender = forms.ChoiceField(label='性别', choices=(('man', '男'), ('women', '女')))
    seek_major = forms.ChoiceField(label='专业',
                                   choices=(
                                       ('software', '软件工程'), ('cs', '计算机科学'), ('jyouhou', '计算机信息'),
                                       ("safety", '计算机安全')))
    seeker_domicile = forms.CharField(label='住址', max_length=120)
    seek_education = forms.ChoiceField(label='教育程度',
                                       choices=(('seniorHighSchool', '高中'), ('college', '本科'), ('postgraduate', '研究生'),
                                                ('doctor', '博士生')))
