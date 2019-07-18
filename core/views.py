from django.shortcuts import render

# Create your views here.

def QuestionListView(request):
    
    question_list = Question.objects.all()

    context ={
        'question_list' : question_list,

    }
    return render(request, 'index.html', context=context)


