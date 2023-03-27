from django.shortcuts import render
from django.views.generic.base import TemplateView

from contents.models import Content

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class ProfileEdit(TemplateView):
    template_name = 'C:/web/django/alpagram/templates/users/porfile.html'
    
    def get_context_data(self, **kwargs):
        """
        로그인 사용자의 작성글 갯수
        """
        context = super().get_context_data(**kwargs)
        context['contents'] = Content.objects.filter(user=self.request.user)
        return context