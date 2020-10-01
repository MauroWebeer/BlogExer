class Postagem:

    rodape = "Editora Teste"

    def __init__(self, id,  titulo, texto, data_public):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.data_public = data_public



    def __str__(self):
        return "id={}, titulo={}, texto={}, data_public={}".format(self.id, self.titulo, self.texto, self.data_public)