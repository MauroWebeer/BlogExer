# Python Object Oriented Exercise

from datetime import datetime
from datetime import timedelta
from Blog import Blog
from Postagem import Postagem
from Usuario import Usuario

usuario = Usuario(1, "Lucas", "slipknust", "knust1000")

login = input("Digite o login do usuario: ")
senha = input("Digite a senha do usuario: ")

if usuario.login != login or usuario.senha != senha:
    print("Usuario ou senha invalidos")
    exit()

blog = Blog()
postagem01 = Postagem(1, "Olá, pessoal!", "Lorem ipsum", datetime.now())
blog.adicionar_postagem(postagem01)
blog.publicar_postagem(postagem01)
postagem02 = Postagem(2, "Essa notícia só vai entrar amanhã", "Lorem lorem", datetime.now() + timedelta(days=1))
blog.adicionar_postagem(postagem02)
postagem03 = Postagem(3, "Essa notícia vai entrar daqui a pouco", "Lorem lorem", datetime.now() + timedelta(hours=1))
blog.adicionar_postagem(postagem03)
blog.publicar_postagem(postagem03)
postagem04 = Postagem(4, "Essa notícia vai entrar e será removida logo após", "Lorem lorem", datetime.now())
blog.adicionar_postagem(postagem04)
blog.apagar_postagem(postagem04)

print("Postagens publicadas:")
for postagem in blog.listar_postagens_public():
    print(postagem)

print("Todas as postagens:")
for postagem in blog.listar_postagens():
    print(postagem)

print(postagem01.rodape)