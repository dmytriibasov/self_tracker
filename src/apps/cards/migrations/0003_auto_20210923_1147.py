# Generated by Django 3.2.7 on 2021-09-23 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('remind_time', models.TimeField(blank=True, default='21:00', null=True)),
                ('remind_date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, default='Add comment here', max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='cards.card')),
            ],
            options={
                'verbose_name': 'Reminder',
                'verbose_name_plural': 'Reminders',
            },
        ),
    ]
