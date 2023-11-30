from django.db import models
from categories.models import Category

# Create your models here.
class Item(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    photo = models.ImageField('Foto', upload_to='photos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering =['id']

    def __str__(self):
        return self.name

