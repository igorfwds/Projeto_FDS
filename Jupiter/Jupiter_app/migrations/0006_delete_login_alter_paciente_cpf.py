# Generated by Django 4.2.5 on 2023-10-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jupiter_app', '0005_paciente_alergias_paciente_altura_paciente_cep_and_more'),
    ]

    operations = [
        # migrations.DeleteModel(
        #     name='Login',
        # ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
