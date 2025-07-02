from django.db import models

NATIONALITY_CHOICES = [
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('OTHER', 'Outro'),
]

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        ordering = ['name']
