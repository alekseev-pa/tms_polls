import time
from django.http.response import HttpResponse
from django.shortcuts import render
from polls.helpers import calculate_sum


def index_view(request):
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse('Your user agent is: {}'.format(user_agent))


def contact_us_view(request):
    welcome_text = 'You opened page'
    result = None
    circles = []

    if request.method == 'POST':
        welcome_text = 'You have submitted form'
        print(request.POST['number_a'])
        number_a = int(request.POST['number_a'])
        number_b = int(request.POST['number_b'])

        result = calculate_sum(number_a, number_b)

        for n in range(result):
            circles.append({
                'name': 'Circle %s' % n,
            })

    context = {
        'current_time': time.strftime('%H:%M:%S %A'),
        'welcome_text': welcome_text,
        'result': result,
        'circles': circles,
    }

    return render(request, 'contact_us.html', context=context)
    # return HttpResponse('Here will be contact us form')


def questions(request):
    from polls.models import Question
    from datetime import datetime

    q = Question(question_text='How do you fel today?', pub_date=datetime.now())
    q.save()

    questions = Question.objects.all()
    return render(request, 'questions.html', context={'questions': questions})
