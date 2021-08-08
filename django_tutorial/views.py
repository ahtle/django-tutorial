from django.views import generic


class Home(generic.TemplateView):
    template_name = 'main/index.html'

