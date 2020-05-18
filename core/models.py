from django.db import models


class Face(models.Model):
    # content = models.TextField()
    face = models.ImageField(default='default.jpg', upload_to='client_faces')

    def __str__(self):
        return self.face.name
