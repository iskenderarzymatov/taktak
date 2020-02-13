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


class DeyatelnostView(TemplateView):
    template_name = 'deyatelnost.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })


class NewsView(TemplateView):
    template_name = 'news.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class PartnersView(TemplateView):
    template_name = 'partners.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class ToursView(TemplateView):
    template_name = 'tours.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })

class ContactusView(TemplateView):
    template_name = 'contactus.html'

    def get(self, request, *args, **kwargs):
        # tours = Tour.objects.all()
        return render(request, self.template_name, context={
            # 'tours': tours,
        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={
        })
