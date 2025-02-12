class Midia:
    quantidade = 0 # atributo de classe

    def __init__(self, titulo:str, autor:str, ano:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        Midia.quantidade += 1

    
    def __str__(self) -> str:
        return f"Midia({self.titulo}, {self.autor}, {self.ano})"

class Livro(Midia):
    def __init__(self,
                 titulo:str,
                 autor:str,
                 ano:str,
                 paginas:int,
                 editora:str
                 ):
        super().__init__(titulo, autor, ano)
        self.paginas = paginas
        self.editora = editora
    
    def __str__(self) -> str:
        return f"Livro({self.titulo}, {self.autor}, {self.ano}, {self.paginas} páginas, Editora {self.editora})"

class Filme(Midia):
    def __init__(self,
                 titulo:str,
                 autor:str,
                 ano:str,
                 diretor:str,
                 duracao:int
                 ):
        super().__init__(titulo, autor, ano)
        self.diretor = diretor
        self.duracao = duracao

    def __str__(self) -> str:
        return f"Filme({self.titulo}, {self.autor}, {self.ano}, Diretor: {self.diretor}, duração: {self.duracao} minutos)"

class Musica(Midia):
    duracao_total = 0

    def __init__(self,
                 titulo:str,
                 autor:str,
                 ano:str,
                 album:str,
                 duracao:float
                 ):
        super().__init__(titulo, autor, ano)
        self.album = album
        self.duracao = duracao
        Musica.duracao_total += duracao
    
    def __str__(self) -> str:
        return f"Musica({self.titulo}, {self.autor}, {self.ano}, Álbum: {self.album}, duração: {self.duracao} minutos)"


l1 = Livro(titulo="Algoritmos",
           autor="Thomas Cormen",
           ano=2004,
           paginas=439,
           editora="Elsevier")
print(l1)

f1 = Filme(titulo="Titanic",
           autor="Fulano",
           ano=1999,
           duracao=120,
           diretor="Fulano")
print(f1)

Musica(titulo="My Heart Will Go On",
            album="Qualquer um",
            ano=1987,
            autor="Fulano",
            duracao=3.5)
Musica(titulo="My Heart Will Go On",
            album="Qualquer um",
            ano=1987,
            autor="Fulano",
            duracao=2.8)
Musica(titulo="My Heart Will Go On",
            album="Qualquer um",
            ano=1987,
            autor="Fulano",
            duracao=4)


print("Duração total das músicas: ", Musica.duracao_total, "minutos")
print("Quantidade de mídias na biblioteca: ", Midia.quantidade)
