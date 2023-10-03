from .models import Articles
from django.forms import  DateTimeInput, ModelForm, TextInput, Textarea

class Articlesform(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class' : 'first',
                'placeholder' : 'Название статьи',

            }),
            'anons': TextInput(attrs={
                'class' : 'first',
                'placeholder' : 'Анонс статьи',
            }),
            'date': DateTimeInput(attrs={
                'class' : 'first',
                'placeholder': 'Дата пубдикации'
            }),
            'full_text': Textarea (attrs={
                'class' : 'second',
                'placeholder' : 'Текст статьи'
            })
        }