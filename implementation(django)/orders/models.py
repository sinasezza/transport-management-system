import uuid
from django.db import models



class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # -----------------------------------------
    