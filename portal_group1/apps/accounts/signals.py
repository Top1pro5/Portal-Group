from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

Groups = ['User', 'Moderator', 'Admin']

@receiver(post_migrate)
def create_groups(sender,**kwargs):
    for name in Groups:
        Group.objects.get_or_create(name=name)