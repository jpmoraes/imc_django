from django.db.models.signals import post_migrate
from django.dispatch import receiver
from home.models import Categoria

@receiver(post_migrate)
def seed_data(sender, **kwargs):
    if sender.name == "home":
        # Cria categorias se não existirem
        Categoria.objects.get_or_create(categoria="Abaixo do peso")
        Categoria.objects.get_or_create(categoria="Normal")
        Categoria.objects.get_or_create(categoria="sobrepeso")
        Categoria.objects.get_or_create(categoria="Obesidade I")
        Categoria.objects.get_or_create(categoria="Obesidade II")
        Categoria.objects.get_or_create(categoria="Obesidade III")