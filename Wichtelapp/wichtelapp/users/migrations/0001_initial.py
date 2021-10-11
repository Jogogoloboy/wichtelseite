# Generated by Django 3.2.6 on 2021-08-21 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, help_text='ohne Adresse kein Wichteln. Falls du über die Feiertage wegfährst, bitte auch eine Ersatzadresse (+Zeitraum) angeben.', null=True, verbose_name='Meine Adresse')),
                ('favoritecolors', models.CharField(blank=True, max_length=250, null=True, verbose_name='Meine Lieblingsfarben')),
                ('favoritematerials', models.CharField(blank=True, max_length=250, null=True, verbose_name='Meine Lieblingsmaterialien')),
                ('favoritesmells', models.CharField(blank=True, max_length=250, null=True, verbose_name='Meine Lieblingsgerüche')),
                ('favoritefood', models.CharField(blank=True, max_length=250, null=True, verbose_name='Meine Lieblingslebensmittel/Getränke')),
                ('favoritestyles', models.CharField(blank=True, max_length=250, null=True, verbose_name='Meine Lieblingsmuster/Motive/Modestile')),
                ('idontlike', models.CharField(blank=True, max_length=500, null=True, verbose_name='Farben/Materialien/Gerüche/Geschmäcker/Muster/Stile, die ich NICHT mag')),
                ('allergies', models.CharField(blank=True, help_text='hier kannst du auch unterbringen, ob du Vegan bist/Alkohol trinkst etc.', max_length=250, null=True, verbose_name='Allergien/Unverträglichkeiten/Ernährungsweisen')),
                ('characters', models.TextField(blank=True, help_text='kurze, knackige Beschreibung deines Charakters, (falls du dir was für einen Char wünscht)', null=True, verbose_name='Von mir bespielte Larp-Charaktere')),
                ('nerdlove', models.CharField(blank=True, max_length=500, null=True, verbose_name='Mein Nerd-Herz schlägt für...')),
                ('accessories', models.CharField(blank=True, help_text='hier kannst du z.B. schreiben, ob du Ohrlöcher hast, generell Haarstäbe benutzt, lieber Mützen als Stirnbänder trägst, etc.', max_length=250, null=True, verbose_name='Diese Arten von Schmuck/Accessoires trage ich im Alltag')),
                ('sizes', models.CharField(blank=True, help_text='natürlich nur für deine Wünsche relevante Daten eintragen, z.B. Handgelenkumfang für Armband-Wunsch oder Kleidergröße für ein T-Shirt-Wunsch', max_length=250, null=True, verbose_name='Meine Maße/Kleidergröße(n)')),
                ('image1', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics', verbose_name='Profilbild')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]