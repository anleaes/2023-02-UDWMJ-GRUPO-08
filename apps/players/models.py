from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereço', max_length=100) 
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('H', 'Humano'),
        ('O', 'Orc'),
        ('E', 'Elfo'),
        ('D', 'Dragonborn'),
        ('A', 'Anoes'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    
    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
        ordering =['id']

    def __str__(self):
        return self.name