from django.db import models
from django.template.defaultfilters import date

class Table(models.Model):
    seats = models.PositiveSmallIntegerField()

    def __str__(self):
        return 'table %s' % self.id

    class Meta:
        verbose_name = 'Стол'
        verbose_name_plural = 'Столы'

class Order(models.Model):
    date = models.DateField()
   
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="table",)
    
    def __str__(self):
        return 'order %s' % self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Stock(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='stock/')
    discount = models.IntegerField(default =0)
    description = models.TextField(blank=True, null=True, default=None)
    start_stock = models.DateField(blank=True,default=None,)
    end_stock = models.DateField(blank=True, default=None,)
    
    def __str__(self):
        return 'stock %s' % self.id
    
    class Meta:
        verbose_name = 'Акция '
        verbose_name_plural = 'Акции'

class CategoryMenu(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='category/', verbose_name='Фото')
   
    def __str__(self):
        return 'category %s' % self.id
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Food(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='food/', verbose_name='Фото')
    portion = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=8, decimal_places=2,  )
    category =  models.ForeignKey(CategoryMenu, verbose_name="Категория",)
 
    def __str__(self):
        return ' %s' % self.name
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
