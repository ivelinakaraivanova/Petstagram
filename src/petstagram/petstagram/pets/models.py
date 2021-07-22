from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

UserModel = get_user_model()

# def is_positive(value):
#     if value <= 0:
#         raise ValidationError


class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DOG, 'Dog'),
        (TYPE_CHOICE_CAT, 'Cat'),
        (TYPE_CHOICE_PARROT, 'Parrot')

    )

    type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()

    # age = models.IntegerField(
    #     null=False,
    #     blank=False,
    #     validators=[
    #         models.Min(1),
    #         # is_positive
    #     ],
    # )

    description = models.TextField()
    # image_url = models.URLField()
    image = models.ImageField(
        upload_to='pets',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


    # def __str__(self):
    #     return f'{self.name}, {self.age}, {self.type}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
