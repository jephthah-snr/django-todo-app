from django import forms
from . models import todoSchema

class addTodoForm(forms.ModelForm):
    class Meta:
        model = todoSchema
        fields = ['name']
        widgets = {
        'name': forms.TextInput(attrs={'placeholder': ('Add item to your todo list')})
        }

# class register(UserCreationForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'example@email.com'}))
#     class Meta():
#         model = User
#         fields = ['username','email','password1','password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'placeholder': _('Username')}),
#             'password1': forms.PasswordInput(attrs={'placeholder': _('password')}),
#             'password2': forms.PasswordInput(attrs={'placeholder': _('password2')}),
#         }
#     def __init__(self, *args, **kwargs):
#         super(register, self).__init__(*args, **kwargs)
#         self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': (_("Password"))})
#         self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': (_("Confirm password"))})