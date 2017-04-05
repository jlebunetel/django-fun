# tutoriel

Je suis le tutoriel issu de la documentation django : (https://docs.djangoproject.com/fr/1.10/intro/tutorial01/).

J'utilise un *virtualenv* avec *Python 3.4.3* dans lequel est installé *Django 1.10.4*.

## création d'un nouveau projet

```bash
$ django-admin startproject graph
```
## lancement du serveur

```bash
$ python manage.py runserver
```

## création de l'application livre de bord

```bash
$ python manage.py startapp livre
```
## modification de settings.py

## création de la base de données

```bash
$ python manage.py migrate
```

## création et activation des modèles

```bash
$ python manage.py makemigrations livre
$ python manage.py migrate

```

le guide en trois étapes pour effectuer des modifications aux modèles :

    Modifiez les modèles (dans models.py).

    Exécutez python manage.py makemigrations pour créer des migrations correspondant à ces changements.

    Exécutez python manage.py migrate pour appliquer ces modifications à la base de données.


django shell


## création d'un utilisateur administrateur

```bash
$ python manage.py createsuperuser
```

## Rendre l’application modifiable via l’interface d’admin
