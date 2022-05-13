from django.db import models

class Report(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField(max_length=1000, null=True, default='Форма была без описания')
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'