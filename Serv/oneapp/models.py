from django.db import models


class Abstract(models.Model):
    name = models.CharField(
        max_length=100
    )

    class Meta:
        abstract = True


class Primarch(Abstract):
    homeworld = models.CharField(
        max_length=100
    )
    alive = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ['pk']


class Chapter(Abstract):
    primarch = models.ForeignKey(
        to=Primarch,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='chapter'
    )

    class Meta:
        ordering = ['pk']
