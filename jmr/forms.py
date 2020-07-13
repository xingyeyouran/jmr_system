from django import forms


class JobForm(forms.Form):
    job_name = forms.CharField(label='职位名', max_length=40)
    job_school = forms.CharField(label='学校要求', max_length=40)
    job_degree = forms.ChoiceField(label='教育程度',
                                   choices=(('1', '高中'), ('2', '本科'), ('3', '研究生'),
                                            ('4', '博士生')))
    job_major = forms.ChoiceField(label='专业',
                                  choices=(
                                      ('software', '软件工程'), ('cs', '计算机科学'), ('jyouhou', '计算机信息'),
                                      ("safety", '计算机安全')))
    job_salary = forms.IntegerField(label='工资')
    job_count = forms.IntegerField(label='招聘人数')
    job_info = forms.CharField(label='相关信息', max_length=200)


class EnterpriseForm(forms.Form):
    enterprise_account = forms.CharField(label='企业账号', max_length=40)
    enterprise_password = forms.CharField(label='企业密码', max_length=40)
    enterprise_name = forms.CharField(label='企业名称', max_length=40)
    enterprise_tel = forms.IntegerField(label='企业电话')
    enterprise_address = forms.CharField(label='企业地址', max_length=120)
    enterprise_mail = forms.EmailField(label='企业邮箱')
    enterprise_info = forms.CharField(label='企业简介', max_length=300)


class UserForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=40)
    user_password = forms.CharField(max_length=40, label='密码', widget=forms.PasswordInput)


class EmployeeForm(forms.Form):
    employee_name = forms.CharField(label='性名', max_length=40)
    employee_account = forms.CharField(label='用户名', max_length=40)
    employee_password = forms.CharField(max_length=40, label='密码')


class ResumeForm(forms.Form):
    resume_birthday = forms.DateTimeField(label='生日')
    resume_race = forms.CharField(label='民族', max_length=4)
    resume_school = forms.CharField(label='学校', max_length=40)
    resume_tel = forms.IntegerField(label='电话')
    resume_mail = forms.EmailField(label='邮箱')
    resume_gender = forms.ChoiceField(label='性别', choices=(('man', '男'), ('women', '女')))
    resume_major = forms.ChoiceField(label='专业',
                                     choices=(
                                         ('software', '软件工程'), ('cs', '计算机科学'), ('jyouhou', '计算机信息'),
                                         ("safety", '计算机安全')))
    resume_address = forms.CharField(label='住址', max_length=120)
    resume_degree = forms.ChoiceField(label='教育程度',
                                      choices=(('seniorHighSchool', '高中'), ('college', '本科'), ('postgraduate', '研究生'),
                                               ('doctor', '博士生')))
    resume_info = forms.CharField(label='更多', max_length=200)
