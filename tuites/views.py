from django.contrib import messages
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from tuites.forms import PostTuiteForm
from tuites.models import Tuite

class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('post_tuite')
    
    def get_initial(self):
        return{
            'user': self.request.user
        }
    
    def form_valid(self, form):
        messages.success(
            self.request,
            'Você postou um tuire'
        )
        return super().form_valid(form)

# Não está sendo utilizado

# def post_tuite(request):
#     context = {}

#     if request.method == 'POST':
#         print('Enviando')
#         # print(request.POST) retorna um dicionário
#         content = request.POST.get('content', None)
        
#         if content == '' or content == ' ':
#             context['error'] = 'Tuite não pode estar vazio'
        
#         else:
#             tuite =  Tuite.objects.create(
#                 content = content,
#                 author = request.user,
#             )
#             context['success_message'] = f'O tweet "{tuite.content}" foi enviado'
        
#         print(content)

#     return render(request, 'post_tuite.html', context)