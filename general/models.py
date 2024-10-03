from django.db import models
from django.utils import timezone 

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set created_at on creation
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super(BaseModel, self).save(*args, **kwargs)


class globalNote(BaseModel):
    student_id = models.CharField(max_length=255, blank=False, null=False)
    comment = models.TextField()