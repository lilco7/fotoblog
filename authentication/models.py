#Importation des modules 
from django.contrib.auth.models import AbstractUser
from django.db import models

#Définition du modèle User personnalisèe

class User(AbstractUser):
    #Définition des constantes de roles pour diférencier nos types d'utilisateurs

    CREATOR = 'CREATOR'
    SUBCRIBER = 'SUBCRIBER'

    ROLES_CHOICES = (
        (CREATOR, 'créateur'),
        (SUBCRIBER, 'abonné'),
    )

    #Ajout des champs suplémentaires photo_profile et role

    photo_profile = models.ImageField(verbose_name=('photo de profile'))
    role = models.CharField(max_length=30, choices=ROLES_CHOICES, verbose_name=('role de l\'utilisateur'))
 
