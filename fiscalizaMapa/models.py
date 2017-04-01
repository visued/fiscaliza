from django.db import models
from django.contrib.gis.db import models

# Create your models here.

ASSUNTO = (
    ('buraco_rua', 'Buraco na rua'),
    ('iluminacao', 'Iluminação'),
    ('lixo_esposto', 'Lixo esposto'),
    ('mato', 'Mato'),
    ('entulho', 'Entulho na rua/calçada'),
    ('sinalizacao', 'Sinalização'),
    ('esgoto_esposto', 'Esgoto exposto'),
)
class Incidente(models.Model):
    criado = models.DateTimeField(auto_now=True)
    assunto = models.CharField(max_length=255, choices=ASSUNTO)
    localizacao = models.PointField(srid=4326)


    objects = models.GeoManager()

    def __str__(self):
        return self.assunto







