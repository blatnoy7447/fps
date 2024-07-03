from tortoise.models import Model
from tortoise import fields


class User(Model):
    username = fields.CharField(max_length=100, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)
