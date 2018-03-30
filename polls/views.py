from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from polls.models import Question, Options

@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    return render(request, 'index.html', {
        'latest_question_list': latest_question_list
    })

@csrf_exempt
def detail(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    if request.user in question.user_voted.all():
        is_voted = True
    else:
        is_voted = False
    if request.method == "GET":
        return render(request, 'details.html', {'question': question, "is_voted": is_voted})
    if request.method == "POST":
        try:
            selected_option = question.options_set.get(id=request.POST['options'])
        except (KeyError, Options.DoesNotExist):
            return render(request, 'details.html', {'question': question,
                                                    'error_message': "You don't select a choice"
                                                    })
        if not is_voted:
            selected_option.votes += 1
            question.user_voted.add(request.user)
            selected_option.save()
        return HttpResponseRedirect(reverse('polls:details', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'results.html', {'question': question})

@csrf_exempt
def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_option = question.options_set.get(id=request.POST['options'])

    except (KeyError, Options.DoesNotExist):
        return render(request, 'details.html', {'question': question,
                                                'error_message': "You don't select a choice"
                                                })
    else:

        selected_option.votes += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


@csrf_exempt
def display(request, question_id):
    label_list, data_list = [], []
    question = Question.objects.get(id=question_id)
    selected_option = question.options_set.all()
    for response in selected_option:
        label_list.append(response.option_text)
        data_list.append(response.votes)
    context = {'default_labels': label_list, 'default_data': data_list}

    return JsonResponse(context)



