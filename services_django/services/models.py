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


class Service(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Categoría",
        help_text="Categoría a la que pertenece el servicio."
    )
    title = models.CharField(
        "Título",
        max_length=200,
        help_text="Nombre del servicio, por ejemplo: 'Corte de cabello'."
    )
    description = models.TextField(
        "Descripción",
        blank=True,
        help_text="Descripción detallada del servicio."
    )
    price = models.DecimalField(
        "Precio",
        max_digits=10,
        decimal_places=2,
        help_text="Precio del servicio."
    )
    duration = models.PositiveIntegerField(
        "Duración",
        help_text="Duración del servicio en minutos."
    )
    is_active = models.BooleanField(
        "Activo",
        default=True,
        help_text="Indica si el servicio está disponible."
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
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["title"]
        unique_together = ['category', 'title']

    def __str__(self):
        return f"{self.title} - {self.category.title}"