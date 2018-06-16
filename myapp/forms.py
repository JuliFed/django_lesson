from django import forms
from .models import Task


class TaskForm(forms.Form):
    text = forms.CharField(max_length=10)
    checked = forms.BooleanField(required=False)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'checked']
        labels = {'text': 'Task Name',
                   'checked': 'Done' }
        # help_texts = {}
        # error_messages = {
        #     "text": {
        #         "max_length": "Error max_length",
        #     }
        # }
        # widgets = {
        #     'text': forms.Textarea(),
        # }

    # def clean(self):
    #     """
    #     Выполняется после валидации в модели!
    #     Дополнительные логические проверки или проверки не учитывающиеся в модели БД
    #     :return:
    #     """
    #     text = self.data['text']
    #     err_text = []
    #     if text.lower() == 'lol':
    #         # raise forms.ValidationError({'text': 'sdfsadf'})
    #         err_text.append('Not lol')
    #
    #     if err_text:
    #         raise forms.ValidationError({'text': err_text})
    #
    # def clean_text(self):
    #     """
    #     Валидация отдельно по каждой филде
    #     :return:
    #     """
    #     text = self.cleaned_data['text']
    #     errors = []
    #     if text == 'LOL':
    #         errors.append('NOT LOL!!!!')
    #
    #     if errors:
    #         raise forms.ValidationError(errors)
