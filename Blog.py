from datetime import datetime
from datetime import timedelta

class Blog:

    def __init__(self):
        self.postagens = []

    def adicionar_postagem(self, postagem):
        self.postagens.append(postagem)

    def publicar_postagem(self, postagem):
        postagem.data_public = datetime.now()
        for postagem_existent in self.postagens:
            if postagem_existent.id == postagem.id:
                self.postagens.remove(postagem_existent)
        self.postagens.append(postagem)

    def listar_postagens_public(self):
        postagens_public = []
        for postagem in self.postagens:
            if postagem.data_public <= datetime.now():
                postagens_public.append(postagem)
        return postagens_public

    def listar_postagens(self):
        return self.postagens

    def apagar_postagem(self, postagem):
        for postagem_existent in self.postagens:
            if postagem_existent.id == postagem.id:
                self.postagens.remove(postagem)
