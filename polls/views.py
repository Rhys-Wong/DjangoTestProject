from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
import csv
from .models import Item

# Create your views here.
def index(request):
    return HttpResponse("Hello")

def bye(request):
    return HttpResponse("Bye")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice_ids = request.POST.getlist("choice")
        res = [eval(i) for i in selected_choice_ids]
        print("Modified list is: ", res)
        selected_choices = question.choice_set.filter(pk__in=selected_choice_ids)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # <--- For vote counting! -->



        # for selected_choices in selected_choices:
        #     selected_choices.votes += 1
        #     selected_choices.save()


        # <-- END -->
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # <-- Saving config to file! -->


        file_path = "config.txt"
        with open(file_path,"w") as file:
            for choice in selected_choices:
                file.write(choice.choicetext + '\n')
        # return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        return HttpResponseRedirect('index.html')

def index1(request):
    return render(request, "polls/index1.html")

# def config(request, config_id):
#     try:
#         question = Config.objects.get(pk=config_id)
#     except Config.DoesNotExist:
#         raise Http404("Config does not exist")
#     return render(request, "polls/config.html")

def index(request):
    question = Question.objects.all()
    return render(request, "polls/index.html", {"latest_question_list" : question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def export_data(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_items[]')
        selected_items = Item.objects.filter(pk__in=selected_ids)

        export_format = request.POST.get('export_format', 'json')

        if export_format == 'json':
            data = [{'name': item.name} for item in selected_items]
            response = JsonResponse(data, safe=False)
            response['Content-Disposition'] = 'attachment; filename="selected_items.json"'
            return response
        elif export_format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="selected_items.csv"'
            writer = csv.writer(response)
            writer.writerow(['Name'])
            for item in selected_items:
                writer.writerow([item.name])
            return response

    items = Item.objects.all()
    return render(request, 'polls/export.html', {'items': items})