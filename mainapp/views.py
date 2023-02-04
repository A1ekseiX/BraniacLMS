from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"


class CoursesPageView(TemplateView):
    template_name = "mainapp/corses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class HelloWorldView(TemplateView):
    def get(self, *args):
        return HttpResponse("Hellow world!")


def check_kwargs(request, **kwargs):
    return HttpResponse(f"kwargs:<br>{kwargs}")
