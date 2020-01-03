from django.views.generic import TemplateView

from home.models import Slider, HomeGallery


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        slider = Slider.objects.filter(is_active=True)
        home_gallery = HomeGallery.objects.filter(is_active=True)
        context = {
            "slider": slider,
            "home_gallery": home_gallery,
        }
        return self.render_to_response(context=context)


class AboutView(TemplateView):
    template_name = 'about/about.html'
