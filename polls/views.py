from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from polls.models import Question, Options


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'index.html', {
        'latest_question_list': latest_question_list
    })


def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    try:
        selected_option = question.options_set.get(id=request.POST['options'])
    except (KeyError, Options.DoesNotExist):
        return render(request, 'details.html', {'question': question,
                                                'error_message': "You don't select a choice"
                                                })
    else:
        if request.method == 'GET':
            Question.user_voted.add(request.user)

            if request.user in Question.user_voted.all():
                is_voted = True
            else:
                is_voted = False
        selected_option.votes += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



