from django.views.generic.base import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"  # 템플릿지정