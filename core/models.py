from django.db import models


class Face(models.Model):
    # content = models.TextField()
    face = models.ImageField(upload_to='client_faces')

    def __str__(self):
        return self.face.name
