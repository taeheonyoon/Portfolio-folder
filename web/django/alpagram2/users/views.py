from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from contents.models import Content

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from . models import TestModel2
from . forms import AuthorForm
import json


@method_decorator(login_required, name='dispatch')
class ProfileEdit(TemplateView):
    template_name = 'C:/web\django/alpagram2/templates/users/profile.html'
    
    def get_context_data(self, **kwargs):
        """
        로그인 사용자의 작성글 갯수
        """
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.filter(user=self.request.user)
        # context['result'] = Content.objects.filter(user=self.request.user)
        return context
    
class Itemtest(CreateView):
    model = TestModel2
    success_url = reverse_lazy('itemtest_index')
    template_name = 'C:/web\django/alpagram2/templates/users/profile.html'
    form_class = AuthorForm

    def get(self, request, *args, **kwargs):
        qs = TestModel2.objects.all().last()
        if qs:
            result = json.loads(qs.test_list)
            print(result, type(result))
            ctx = {'result' : result}
            return self.render_to_response(ctx)
    
    
    def form_valid(self, form):
        test = form.save(commit=False)
        test.test_list = json.dumps(self.request.POST.getlist('test_list'))
        test.user = self.request.user
        test.save()
        return super().form_valid(form)