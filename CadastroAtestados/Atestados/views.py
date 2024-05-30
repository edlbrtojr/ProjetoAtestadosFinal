from django.shortcuts import render, redirect
from .forms import AtestadoForm
from .models import Atestado
from .forms import AtestadoFilterForm


def cadastrar_atestado(request):
    if request.method == 'POST':
        form = AtestadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('lista_atestados')
    else:
        form = AtestadoForm()

    return render(request, 'cadastrar_atestado.html', {'form': form})

def lista_atestados(request):
    form = AtestadoFilterForm(request.GET)
    atestados = Atestado.objects.all()

    if form.is_valid():
        nome_aluno = form.cleaned_data.get('nome_aluno')
        data_afastamento = form.cleaned_data.get('data_afastamento')
        turma_aluno = form.cleaned_data.get('turma_aluno')
        ano_aluno = form.cleaned_data.get('ano_aluno')

        if nome_aluno:
            atestados = atestados.filter(nome_aluno__icontains=nome_aluno)

        if data_afastamento:
            atestados = atestados.filter(data_atestado=data_afastamento)

        if turma_aluno:
            atestados = atestados.filter(turma_aluno=turma_aluno)

        if ano_aluno:
            atestados = atestados.filter(ano_aluno=ano_aluno)

    return render(request, 'lista_atestados.html', {'atestados': atestados, 'form': form})

def inicio(request):
    total_atestados = Atestado.objects.count()
    ultimos_atestados = Atestado.objects.order_by('-id')[:5]
    return render(request, 'inicio.html', {'total_atestados': total_atestados, 'ultimos_atestados': ultimos_atestados})