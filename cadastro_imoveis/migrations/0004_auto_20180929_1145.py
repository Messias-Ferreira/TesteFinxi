# Generated by Django 2.1.1 on 2018-09-29 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_imoveis', '0003_auto_20180929_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagens', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='endereco',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro_imoveis.Endereco'),
        ),
        migrations.AlterField(
            model_name='imoveis',
            name='imagens',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro_imoveis.Imagens'),
        ),
    ]