from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone


class Wish(models.Model):

    CATEGORY_CHOICES= [
    ('kitchen', 'Gruß aus der Küche'),
    ('clothing', 'Kleidung'),
    ('accessory', 'Accessoires'),
    ('cosmetic', 'Kosmetik & Wellness'),
    ('papier', 'Schriftstücke & Bilder'),
    ('deko', 'Deko'),
    ('hhitem', 'Haushalt'),
    ('other', 'Sonstiges'),
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Anfängerfreundlich'),
        ('medium', 'Anspruchsvoll'),
        ('hard', 'Schwierig'),
    ]
     

# Vom User auszufüllende Felder
    title = models.CharField(unique=True, max_length=200, verbose_name = 'Titel', help_text = 'Gibt deinem Wunsch einen kurzen, knackigen Titel')
    description = models.TextField(verbose_name = 'Beschreibung', help_text = 'Beschreibe deinen Wunsch')
    category = models.CharField(verbose_name='Kategorie', choices=CATEGORY_CHOICES, max_length=100)
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES, max_length=100, verbose_name = 'Schwierigkeitslevel', help_text = 'Deine Einschätzung: schafft das auch ein Anfänger? Oder sollte man etwas mehr Erfahrung haben?')

# Berechnete/automatisch gefüllte Felder
    wisher = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='wisher')
    state = models.CharField(max_length=100, default='Open')
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(null=True, blank=True, default=timezone.now)
    taken = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    sent = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    received = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    secret_santa = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='secret_santa')
    trackingnr = models.CharField(max_length=100, null=True, blank=True)