from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente  # Certifique-se de ter o modelo Cliente corretamente importado

def cadastrar_cliente(request):
    if request.method == 'POST':
        # Coletando os dados do formulário
        nome_completo = request.POST.get('nome_completo')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')
        instituicao_escolar = request.POST.get('instituicao_escolar')
        serie = request.POST.get('serie')
        sexo = request.POST.get('sexo')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        cidade = request.POST.get('cidade')
        regiao = request.POST.get('regiao')
        cep = request.POST.get('cep')

        nome_responsavel = request.POST.get('nome_responsavel')
        cpf_responsavel = request.POST.get('cpf_responsavel')
        rg_responsavel = request.POST.get('rg_responsavel')
        email_responsavel = request.POST.get('email_responsavel')
        telefone_responsavel = request.POST.get('telefone_responsavel')
        data_nascimento_responsavel = request.POST.get('data_nascimento_responsavel')
        profissao_responsavel = request.POST.get('profissao_responsavel')
        sexo_responsavel = request.POST.get('sexo_responsavel')

        # Criando um novo registro no banco de dados
        Cliente.objects.create(
            nome_completo=nome_completo,
            email=email,
            telefone=telefone,
            data_nascimento=data_nascimento,
            instituicao_escolar=instituicao_escolar,
            serie=serie,
            sexo=sexo,
            endereco=endereco,
            numero=numero,
            complemento=complemento,
            cidade=cidade,
            regiao=regiao,
            cep=cep,
            nome_responsavel=nome_responsavel,
            cpf_responsavel=cpf_responsavel,
            rg_responsavel=rg_responsavel,
            email_responsavel=email_responsavel,
            telefone_responsavel=telefone_responsavel,
            data_nascimento_responsavel=data_nascimento_responsavel,
            profissao_responsavel=profissao_responsavel,
            sexo_responsavel=sexo_responsavel
        )

           
        return redirect('clientes')
    
    else:

        return render(request, 'cadastro-clientes.html')

def listar_clientes(request):
    clientes = Cliente.objects.all()  
    return render(request, 'clientes.html', {'clientes': clientes})  

