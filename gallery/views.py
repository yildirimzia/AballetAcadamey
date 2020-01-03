from django.views.generic import TemplateView
from gallery.models import Gallery

class GalleryView(TemplateView):
    template_name = 'gallery/index.html'

    def get(self, request, *args, **kwargs):
        gallery = Gallery.objects.filter(is_active=True)
        context = {
            "gallery": gallery,
        }
        return self.render_to_response(context=context)
