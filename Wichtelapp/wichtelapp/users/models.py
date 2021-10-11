from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    address = characters = models.TextField(verbose_name= 'Meine Adresse', help_text = 'ohne Adresse kein Wichteln. Falls du über die Feiertage wegfährst, bitte auch eine Ersatzadresse (+Zeitraum) angeben.', blank=False, null=True)
    favoritecolors = models.CharField(max_length=250, verbose_name= 'Meine Lieblingsfarben', blank=True, null=True)
    favoritematerials = models.CharField(max_length=250, verbose_name= 'Meine Lieblingsmaterialien', blank=True, null=True)
    favoritesmells = models.CharField(max_length=250, verbose_name= 'Meine Lieblingsgerüche', blank=True, null=True)
    favoritefood = models.CharField(max_length=250, verbose_name= 'Meine Lieblingslebensmittel/Getränke', blank=True, null=True)
    favoritestyles = models.CharField(max_length=250, verbose_name= 'Meine Lieblingsmuster/Motive/Modestile', blank=True, null=True)
    idontlike = models.CharField(max_length=500, verbose_name= 'Farben/Materialien/Gerüche/Geschmäcker/Muster/Stile, die ich NICHT mag', blank=True, null=True)
    allergies = models.CharField(max_length=250, verbose_name= 'Ich bin allergisch auf.../ich verzichte auf.../ich vertrage ... nicht', help_text='hier kannst du auch unterbringen, ob du Vegan bist/Alkohol trinkst etc.', blank=True, null=True)
    characters = models.TextField(verbose_name= 'Von mir bespielte Larp-Charaktere', help_text = 'kurze, knackige Beschreibung deines Charakters, (falls du dir was für einen Char wünscht)', blank=True, null=True)
    nerdlove = models.CharField(max_length=500, verbose_name= 'Mein Nerd-Herz schlägt für...', blank=True, null=True)
    accessories = models.CharField(max_length=250, verbose_name= 'Diese Arten von Schmuck/Accessoires trage ich im Alltag', help_text = 'hier kannst du z.B. schreiben, ob du Ohrlöcher hast, generell Haarstäbe benutzt, lieber Mützen als Stirnbänder trägst, etc.', blank=True, null=True)
    sizes = models.CharField(max_length=250, verbose_name= 'Meine Maße/Kleidergröße(n)', help_text = 'natürlich nur für deine Wünsche relevante Daten eintragen, z.B. Handgelenkumfang für Armband-Wunsch oder Kleidergröße für ein T-Shirt-Wunsch', blank=True, null=True)
    pinterest = models.URLField(verbose_name= 'Link zu deinem Pinterest-Account', max_length=200, blank=True, null=True)
    other = models.TextField(verbose_name= 'Sonstiges', help_text = 'hier ist Platz für weitere Anmerkungen', blank=True, null=True)
    image1 = models.ImageField(verbose_name= 'Bild 1', upload_to='profile_pics', blank=True, null=True, default='default.jpg')
    image2 = models.ImageField(verbose_name= 'Bild 2', upload_to='profile_pics', blank=True, null=True, default='default.jpg')
    image3 = models.ImageField(verbose_name= 'Bild 3', upload_to='profile_pics', blank=True, null=True, default='default.jpg') 

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs): 
        super(Profile,self).save(*args,**kwargs)

        img1 = Image.open(self.image1.path)
        img2 = Image.open(self.image2.path)
        img3 = Image.open(self.image3.path)

        if img1.height > 800 or img1.width > 800:
            output_size = (800, 800)
            img1.thumbnail(output_size)
            img1.save(self.image1.path)

        if img2.height > 800 or img2.width > 800:
            output_size = (800, 800)
            img2.thumbnail(output_size)
            img2.save(self.image2.path)

        if img3.height > 800 or img3.width > 800:
            output_size = (800, 800)
            img3.thumbnail(output_size)
            img3.save(self.image3.path)