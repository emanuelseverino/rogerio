from django.db import models


class Premio(models.Model):
    imagem = models.ImageField(upload_to='premios')
    pontos = models.IntegerField()
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    criado_em: models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
