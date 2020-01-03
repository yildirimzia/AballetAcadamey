from django.views.generic import TemplateView

from blog.models import Blog


class BlogView(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        blog = Blog.objects.filter(is_active=True)[0]
        context = {
            "blog": blog
        }
        return self.render_to_response(context=context)
