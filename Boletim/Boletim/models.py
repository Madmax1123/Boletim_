from django.db import models

class Boletim(models.Model):
    disciplina = models.CharField(max_length=60)
    nota1 = models.DecimalField(max_digits=2, decimal_places=0)
    nota2 = models.DecimalField(max_digits=2, decimal_places=0)
    nota3 = models.DecimalField(max_digits=2, decimal_places=0)
    nota4 = models.DecimalField(max_digits=2, decimal_places=0)
    class Meta:
        verbose_name_plural = 'Notas'

    def __str__(self):
            return '{}'.format(self.nota1 + self.nota2 + self.nota3 + self.nota4 / 4)
