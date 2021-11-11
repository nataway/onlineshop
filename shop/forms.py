from django import forms

class PostForm(forms.Form):
    tittle = forms.CharField(label="Tiêu đề")
    email_receive = forms.CharField(label="Mail nhận")
    body = forms.CharField(label="Nội dung",max_length="1000")