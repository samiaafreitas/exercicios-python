class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.paginas_lidas = 0

    def ler(self, quantidade):
        self.paginas_lidas += quantidade
        if self.paginas_lidas > self.paginas:
            self.paginas_lidas = self.paginas

    def progresso(self):
        porcentagem = self.paginas_lidas / self.paginas * 100
        print(f"{self.titulo}: {porcentagem:.1f}% lido ({self.paginas_lidas}/{self.paginas})")


livro = Livro("Dom Casmurro", "Machado de Assis", 256)
livro.progresso()
livro.ler(64)
livro.progresso()
livro.ler(300)
livro.progresso()
