from django import forms
from .models import Survey, Question, Response, Answer

class SurveyForn(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type', 'order']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [] #поля будут добавляться автоматически

    def __init__(self, *args, **kwargs):
        self.survey = kwargs.pop('survey')
        super().__init__(*args, **kwargs)

    #динамически создаем поля для каждого вопроса
        for question in self.survey.questions.all().order_by('order'):
            if question.question_type == 'text':
                self.fields[f'question_{question.id}'] = forms.CharField(
                    label=question.text, 
                    widget=forms.Textarea(attrs={'rows':3}), 
                    required=True
                )
            elif question.question_type == 'single':
                self.fields[f'question_{question.id}'] = forms.ModelChoiceField(
                    label=question.text, 
                    queryset=question.choices.all(),
                    widget=forms.RadioSelect, 
                    required=True
                )
            elif question.question_type == 'multiple':
                self.fields[f'question_{question.id}'] = forms.ModelMultipleChoiceField(
                    label=question.text,
                    queryset=question.choices.all(),
                    widget=forms.CheckboxSelectMultiple,
                    required=True
                )