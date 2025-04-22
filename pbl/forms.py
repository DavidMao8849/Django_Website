from django import forms
from .models import Member, Friend

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'photo', 'student_id', 'hobby']  # 입력받을 필드 정의
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름'}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '학번'}),
            'hobby': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '취미'}),
        }

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'relation', 'member']  # 입력받을 필드 정의
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '친구 이름'}),
            'relation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '관계'}),
            'member': forms.Select(attrs={'class': 'form-control'}),  # ForeignKey 필드는 드롭다운으로 표시
        }
