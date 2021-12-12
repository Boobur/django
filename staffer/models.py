from django.db import models

# Модел Vendor
class Vendor(models.Model):
    surname = models.CharField(max_length = 30, verbose_name="Фамилия")
    name = models.CharField(max_length = 30, verbose_name="Имя")
    phone = models.CharField(max_length = 13, verbose_name="Телефон номер")
    email = models.EmailField(max_length = 250, verbose_name="Е-майл")
    address = models.CharField(max_length = 250, verbose_name="Адрес")

    # Строковой вывод
    def __str__(self):
        return self.surname

     #Мета таг для настройки админ окна
    class Meta:
        verbose_name =  'Продовец'
        verbose_name_plural = 'Продавции авто'
        #ordering = ['-created_at']


# Модел Customer
class Customer(models.Model):
    surname = models.CharField(max_length = 30, verbose_name="Фамилия")
    name = models.CharField(max_length = 30, verbose_name="Имя")
    phone1 = models.CharField(max_length = 13, verbose_name="Телефон номер 1")
    phone2 = models.CharField(max_length = 13, blank=True, verbose_name="Телефон номер 2")
    email = models.EmailField(max_length = 250, verbose_name="Е-майл")
    address = models.CharField(max_length = 250, verbose_name="Адрес")

    # Строковой вывод
    def __str__(self):
        return self.surname
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        #ordering = ['-created_at']


# Модел Car info
class CarInfo(models.Model):
    car_name = models.CharField(max_length = 30, verbose_name="Наименование")
    car_colors = models.CharField(max_length = 250, verbose_name="Цвета")
    description = models.CharField(max_length = 250, verbose_name="Описание")
    full_text = models.TextField(verbose_name="Полная описание")
    car_photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank=True, verbose_name="фото авто")
    car_category = models.ForeignKey('CarCategory', on_delete=models.PROTECT, null=True, verbose_name = 'Типы авто')

    # Строковой вывод
    def __str__(self):
        return self.car_name
    
    class Meta:
        verbose_name = 'Инф. авто'
        verbose_name_plural = 'Инф. авто'
        #ordering = ['-created_at']

# Модел Car category

class CarCategory(models.Model):
    car_type  = models.CharField(max_length = 150, db_index = True, verbose_name='Наименование категории')
    # Строковой вывод
    def __str__(self):
        return self.car_type
    #Мета таг для настройки админ окна
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        #ordering = ['title']

# Модел Car Base
class CarBase(models.Model):
    car_name = models.CharField(max_length = 30, verbose_name="Наименование")
    car_position = models.IntegerField(verbose_name = "Позиция автомобиля")
    car_color = models.CharField(max_length = 30, verbose_name="Цвета")
    car_date = models.IntegerField(verbose_name = "Год выпуска")
    car_vin = models.CharField(max_length = 17, verbose_name="Идт. Авто")
    car_status =  models.BooleanField(default = False, verbose_name ='Статус')

    # Строковой вывод
    def __str__(self):
        return self.car_name

    class Meta:
        verbose_name = 'База машин'
        verbose_name_plural = 'База машин'
        #ordering = ['-created_at']

#Car summ
class CarSum(models.Model):
    car_name = models.CharField(max_length = 30, verbose_name="Наименование")
    car_position = models.IntegerField(verbose_name = "Позиция автомобиля")
    car_summ = models.IntegerField(verbose_name = "Стоимость авто")

    # Строковой вывод
    def __str__(self):
        return self.car_name
    
    class Meta:
        verbose_name = 'Сумма'
        verbose_name_plural = 'Сумма'
        #ordering = ['-created_at']


#Car order
class CarOrder2(models.Model):
    cust_surname = models.CharField(max_length = 30, verbose_name="Фамилия")
    cust_name = models.CharField(max_length = 30, verbose_name="Имя")
    cust_phone = models.CharField(max_length = 13, verbose_name="Телефон номер")
    car_name = models.CharField(max_length = 30, verbose_name="Наименование")
    car_color = models.CharField(max_length = 30, verbose_name="Цвет авто")
    car_position = models.IntegerField(verbose_name = "Позиция авто")
    car_year =  models.IntegerField(verbose_name = "Год выпуска")
    payment = models.CharField(max_length = 30, verbose_name="Вид оплаты")
    quantity = models.IntegerField(verbose_name = "Количество")
    order_date =  models.DateTimeField(auto_now_add = True, verbose_name ='Дата заказа')

    # Строковой вывод
    def __str__(self):
        return self.car_name
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        #ordering = ['-created_at']



#Color
class Color(models.Model):
    colors = models.CharField(max_length = 30, verbose_name="Цвет")
    # Строковой вывод
    def __str__(self):
        return self.colors
    
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'
        #ordering = ['-created_at']

#Sales info
class SalesInfo2(models.Model):
    car_name = models.CharField ( max_length = 30, verbose_name="Наименование")
    car_category = models.ForeignKey('CarCategory', on_delete=models.PROTECT, null=True, verbose_name = 'Типы авто')
    sales_date =  models.DateTimeField(auto_now_add = True, verbose_name ='Дата продажи')
    sales_sum = models.IntegerField(verbose_name = "Сумма продажи")

    



   

