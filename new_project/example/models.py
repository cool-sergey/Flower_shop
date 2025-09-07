from django.db import models
from users.models import User

class FlowerType(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    description = models.TextField(null = True, blank = True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    quantity = models.PositiveIntegerField(default = 0)
    image = models.ImageField(upload_to = 'flowers_images')
    type = models.ForeignKey(to = FlowerType, on_delete = models.CASCADE )
    def __str__(self):
        return f"{self.name} | category: {self.type.name}"
    
class Bucket(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE)
    product = models.ForeignKey(to = Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 0)
    created_timestamp = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return f'Пользователь {self.user.email} | Продукт: {self.product.name} '
    

## у нас есть фикстуры, это типо экзмепляр
# 
#  базы данных, которую мы можем загрузить при помощи команды
# manage.py loaddata <путь до фикстуры>
