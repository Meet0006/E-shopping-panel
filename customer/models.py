from django.db import models


class Register(models.Model):
	name    = models.CharField(max_length=30)
	email   = models.CharField(max_length=50)
	contact = models.BigIntegerField()

	class Meta:
		db_table = 'register'

