from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
    
    @abstractmethod
    def __repr__(self) -> str:
        pass

class Livro(Publicacao):
    def __init__(self, titulo: str, autor: str, numero_paginas: int):
        super().__init__(titulo, autor)
        self.numero_paginas = numero_paginas
    
    def __repr__(self) -> str:
        return f"Livro: {self.titulo} ({self.autor}), nº de páginas: {self.numero_paginas}"

class Artigo(Publicacao):
    def __init__(self, titulo: str, autor: str, revista: str):
        super().__init__(titulo, autor)
        self.revista = revista
    
    def __repr__(self) -> str:
        return f"Artigo: {self.titulo}, {self.autor}, revista: {self.revista}"

class Revista(Publicacao):
    def __init__(self, titulo: str, autor: str, edicao: int):
        super().__init__(titulo, autor)
        self.edicao = edicao

    def __repr__(self) -> str:
        return f"Revista: {self.titulo}, {self.autor}, {self.edicao}"

l1 = Livro(
    titulo="O Senhor dos Anéis",
    autor="Tolkien",
    numero_paginas=300
    )
a1 = Artigo(
    titulo="Attention is all you need",
    autor="Ashish Vaswani",
    revista="Google"
    )
r1 = Revista(
    titulo="Nature",
    autor="Flora Graham",
    edicao=543
    )

publicacoes: list[Publicacao] = [l1, a1, r1] 
print(publicacoes)
