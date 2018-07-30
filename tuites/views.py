from django.shortcuts import render
from tuites.models import Tuite

def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando')
        # print(request.POST) retorna um dicionário
        content = request.POST.get('content', None)
        
        if content == '' or content == ' ':
            context['error'] = 'Tuite não pode estar vazio'
        
        else:
            tuite =  Tuite.objects.create(
                content = content,
                author = request.user,
            )
            context['success_message'] = f'O tweet "{tuite.content}" foi enviado'
        
        print(content)

    return render(request, 'post_tuite.html', context)