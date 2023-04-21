# Generated by Django 4.1.7 on 2023-04-21 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_alter_event_contato_alter_event_max_ingressos'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=29.99, max_digits=10),
            preserve_default=False,
        ),
    ]
