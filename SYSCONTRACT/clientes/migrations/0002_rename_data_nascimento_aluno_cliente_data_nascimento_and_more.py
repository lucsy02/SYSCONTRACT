# Generated by Django 5.1.1 on 2024-10-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='data_nascimento_aluno',
            new_name='data_nascimento',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='email_aluno',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='bairro',
            new_name='regiao',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='serie_escolar',
            new_name='serie',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nome_aluno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='sexo_aluno',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefone_aluno',
        ),
        migrations.AddField(
            model_name='cliente',
            name='nome_completo',
            field=models.CharField(default='Desconhecido', max_length=255),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro'), ('Prefiro não responder', 'Prefiro não responder')], default='Prefiro não responder', max_length=21),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='Desconhecido', max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf_responsavel',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='instituicao_escolar',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome_responsavel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='profissao_responsavel',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rg_responsavel',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo_responsavel',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outro', 'Outro'), ('Prefiro não responder', 'Prefiro não responder')], default='Prefiro não responder', max_length=21),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone_responsavel',
            field=models.CharField(default='Desconhecido', max_length=15),
        ),
    ]
