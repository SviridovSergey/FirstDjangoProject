from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Survey, Response, Answer
from .forms import ResponseForm
    
# Create your views here.

class SurveyListView(ListView):
    model = Survey
    template_name = 'polls/survey_list.html'
    context_object_name = 'surveys'

    def get_queryset(self):
        return Survey.objects.filter(is_active=True)
    
def survey_detail(request, survey_id):
    survey = get_list_or_404(Survey, id=survey.id, is_active=True)

    if request.method=='POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = Response.objects.create(
                survey=survey,
                user_ip=response.META.get('REMOTE_ADDR')
            )

            #сохраняем ответы на вопросы
            for question in survey.questions.all():
                field_name = f'question_{question.id}'
                answer_value = form.cleaned_data[field_name]

                answer = Answer.objects.create(
                    response=response,
                    question=question
                )

                if question.question.type == 'text':
                    answer.text_answer = answer_value
                    answer.save()
                elif question.question_type == 'single':
                    answer.choices.add(answer_value)
                elif question.question_type == 'multiple':
                    for choice in answer_value:
                        answer.choices.add(choice)

        return redirect('suret_thank_you', response_id=response.id())
    else:
        form = ResponseForm(survey=survey)
    
    return render(request, 'polls/sruvey_detail.html', {
        'survey': survey,
        'form': form
    })

def thank_you(request, response_id):
    response = get_list_or_404(Response, id=response_id)
    return render(response, 'polls/thank_you.html', {'response': response})