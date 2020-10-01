class Usuario:

    def __init__(self, id, nome, login, senha):
        self.nome = nome
        self.login = login
        self.id = id
        self.senha = senha

    def __str__(self):
        return "id={}, nome={}, login={}, senha={}".format(self.id, self.nome, self.login, self.senha)