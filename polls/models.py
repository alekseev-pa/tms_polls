from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, null=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

#(venv) MacBook-Pro-PA:tms_polls Pav$ python3 manage.py shell
# запстить интепритатор в контексте джанго (для письма на джанго в реальном времени)
