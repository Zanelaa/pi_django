# Generated by Django 4.1 on 2022-10-04 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_cardapio_refeicoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='refeicoes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.refeicoes'),
            preserve_default=False,
        ),
    ]