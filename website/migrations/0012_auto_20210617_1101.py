# Generated by Django 3.2.4 on 2021-06-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210607_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='amplitude',
            field=models.CharField(choices=[('PÉSSIMO', 'PÉSSIMO'), ('MAU', 'MAU'), ('BOM', 'BOM'), ('MUITO BOM', 'MUITO BOM'), ('EXCELENTE', 'EXCELENTE')], default='BOM', max_length=10),
        ),
        migrations.AddField(
            model_name='comentario',
            name='classificação',
            field=models.CharField(choices=[('PÉSSIMO', 'PÉSSIMO'), ('MAU', 'MAU'), ('BOM', 'BOM'), ('MUITO BOM', 'MUITO BOM'), ('EXCELENTE', 'EXCELENTE')], default='BOM', max_length=10),
        ),
        migrations.AddField(
            model_name='comentario',
            name='lógica',
            field=models.CharField(choices=[('PÉSSIMO', 'PÉSSIMO'), ('MAU', 'MAU'), ('BOM', 'BOM'), ('MUITO BOM', 'MUITO BOM'), ('EXCELENTE', 'EXCELENTE')], default='BOM', max_length=10),
        ),
        migrations.AddField(
            model_name='comentario',
            name='precisão',
            field=models.CharField(choices=[('PÉSSIMO', 'PÉSSIMO'), ('MAU', 'MAU'), ('BOM', 'BOM'), ('MUITO BOM', 'MUITO BOM'), ('EXCELENTE', 'EXCELENTE')], default='BOM', max_length=10),
        ),
        migrations.AddField(
            model_name='comentario',
            name='profundidade',
            field=models.CharField(choices=[('PÉSSIMO', 'PÉSSIMO'), ('MAU', 'MAU'), ('BOM', 'BOM'), ('MUITO BOM', 'MUITO BOM'), ('EXCELENTE', 'EXCELENTE')], default='BOM', max_length=10),
        ),
    ]
