from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })