from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday

BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {'birthday': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})}

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]
    
    def clean(self):
        super().clean()
        first_name = self.cleaned_data['first_name']
        second_name = self.cleaned_data['second_name']

        if f'{first_name} {second_name}' in BEATLES:
            raise ValidationError(
                "Введите настоящее имя!"
            )
