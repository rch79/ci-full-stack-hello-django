from django.db import models

# Create your models here.
class Item(models.Model):       # inherits Django base model class
    name = models.CharField(max_length=50, null=False, blank=False)  # null and blank equals False prevent items from being created without a name and make the field required on forms, respectively
    done = models.BooleanField(null=False, blank=False, default=False)  # default = false causes to do list items to be marked as not done by default

    def __str__(self):
        return self.name    # returns Item class' name attribute /9overriding the string methid in the base model class, which returns the item object)
