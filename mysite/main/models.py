from django.db import models

# Create your models here.

class HomeSliderActive(models.Model):

    name1 = models.CharField('HomeSliderActive name1', max_length=60)
    name2 = models.CharField('HomeSliderActive name2', max_length=60)
    text = models.TextField('HomeSliderActive text')
    img = models.ImageField('HomeSlider image', upload_to='images')
    logo = models.ImageField('HomeSlider logo', upload_to='images')

    def __str__(self):
        return self.name1
    
class HomeSlider(models.Model):

    name1 = models.CharField('HomeSlider name1', max_length=60)
    name2 = models.CharField('HomeSlider name2', max_length=60)
    text = models.TextField('HomeSlider text')
    img = models.ImageField('HomeSlider image', upload_to='images')
    logo = models.ImageField('HomeSlider logo', upload_to='images')

    def __str__(self):
        return self.name1
    

class Category(models.Model):

    name = models.CharField('Category name', max_length=50)


    def __str__(self):
        return self.name
    
class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ')
    name = models.CharField('SubCategory name', max_length=60)
    price = models.PositiveIntegerField('SubCategory price')
    img = models.ImageField('SubCategory image', upload_to='images')

    def __str__(self):
        return self.name