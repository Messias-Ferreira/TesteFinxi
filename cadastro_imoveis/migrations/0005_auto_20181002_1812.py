# Generated by Django 2.1.1 on 2018-10-02 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_imoveis', '0004_auto_20180929_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagens',
            old_name='imagens',
            new_name='imagem1',
        ),
        migrations.AddField(
            model_name='imagens',
            name='imagem2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='imagens',
            name='imagem3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='imagens',
            name='imagem4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='endereco',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro_imoveis.Endereco'),
        ),
    ]
