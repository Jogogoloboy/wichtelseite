# Generated by Django 3.2.6 on 2021-08-21 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Gibt deinem Wunsch einen kurzen, knackigen Titel', max_length=200, unique=True, verbose_name='Titel')),
                ('description', models.TextField(help_text='Beschreibe deinen Wunsch', verbose_name='Beschreibung')),
                ('category', models.CharField(choices=[('kitchen', 'Gruß aus der Küche'), ('clothing', 'Kleidung'), ('accessory', 'Accessoires'), ('cosmetic', 'Kosmetik & Wellness'), ('papier', 'Bücher und Schriftstücke'), ('deko', 'Deko'), ('other', 'Sonstiges')], max_length=100, verbose_name='Kategorie')),
                ('difficulty', models.CharField(choices=[('easy', 'Anfängerfreundlich'), ('medium', 'Anspruchsvoll'), ('hard', 'I could never...')], help_text='Deine Einschätzung: muss man in der Technik schon sehr bewandert sein, oder schafft das auch ein Anfänger?', max_length=100, verbose_name='Schwierigkeitslevel')),
                ('state', models.CharField(default='Open', max_length=100)),
                ('is_visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('taken', models.DateTimeField(blank=True, null=True)),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('received', models.DateTimeField(blank=True, null=True)),
                ('trackingnr', models.CharField(default='keine', max_length=100)),
                ('secret_santa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secret_santa', to=settings.AUTH_USER_MODEL)),
                ('wisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wisher', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]