from django.db import models

class Client (models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20, default='Кыргызстан')
    birth_year = models.DateField
    work_place = models.CharField(max_length=30)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Account(models.Model):
    number = models.IntegerField(max_length=16, default=0)
    account_type = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Credit(models.Model):
    my_field_name = models.CharField(max_length=255, verbose_name='loans', help_text="Введите строковое значение")
    sum = models.IntegerField(default=0)
    date =models.DateTimeField(auto_now=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Мой кредит'
        verbose_name_plural = 'Мои кредиты'
