# Create your views here.
from django.template.loader import render_to_string, get_template
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from make.models import Make, Model, Generation, Comment


def home(request):

    make = Make.objects.order_by('name')

    return render_to_response('index.html', {'makes': make})


def make(request, make_id=1):

    make = Make.objects.get(id = make_id)
    models = Model.objects.filter(make_id = make_id )

    return render_to_response('make.html', {'make': make, 'models': models})


def model(request):

    generations = Generation.objects.filter(model_id = 1 )
    
    return render_to_response('model.html', {'generations': generations})

#generation_id = 1
def generation(request):

    generation_id = 1
    comments = Comment.objects.filter(generation_id = generation_id )

    return render_to_response('model.html', {'comments': comments})




def vw(request):
    view = "VW"
    html = "<html><body><div>%s Das auto</body></html></div>" % view
    return HttpResponse(html)

def audi(request, make_id = 1):
    view = 'More good than vw'
    #t = get_template('audiview')
    #html = t.render(Context ({'name': view}))
    #return HttpResponse(html)

    return render_to_response('audiview.html', {'name': view})