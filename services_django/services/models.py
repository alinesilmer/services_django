from django.db import models

class Category(models.Model):
    title = models.CharField(
        "Título",
        max_length=100,
        unique=True,
        help_text="Nombre de la categoría, por ejemplo: 'Belleza'."
    )
    icon = models.CharField(
        "Ícono",
        max_length=50,
        help_text="Identificador del ícono, por ejemplo: 'scissors'."
    )
    created_at = models.DateTimeField(
        "Creado el",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Actualizado el",
        auto_now=True
    )

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["title"]

    def __str__(self):
        return self.title
