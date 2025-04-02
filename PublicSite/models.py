from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.TextField()
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=100)

    class Meta:
        db_table = "usuarios"
