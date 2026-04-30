class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def is_disponivel(self):
        return self.__disponivel

    def set_disponivel(self, status):
        self.__disponivel = status

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"{self.__titulo} - {self.__autor} ({status})"

class Usuario:
    def __init__(self, nome):
        self.__nome = nome
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_livros(self):
        return self.__livros_emprestados

    def adicionar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def remover_livro(self, livro):
        self.__livros_emprestados.remove(livro)

    def __str__(self):
        return f"Usuário: {self.__nome}"


class Biblioteca:
    def __init__(self):
        self.__livros = []

    def cadastrar_livro(self, livro):
        self.__livros.append(livro)
        print(f"Livro '{livro.get_titulo()}' cadastrado.")

    def listar_livros(self):
        print("\nLista de livros:")
        for livro in self.__livros:
            print(livro)

    def emprestar_livro(self, usuario, livro):
        if len(usuario.get_livros()) >= 3:
            print(f"{usuario.get_nome()} já possui 3 livros.")
            return

        if not livro.is_disponivel():
            print(f"O livro '{livro.get_titulo()}' já está emprestado.")
            return

        livro.set_disponivel(False)
        usuario.adicionar_livro(livro)
        print(f"Livro '{livro.get_titulo()}' emprestado para {usuario.get_nome()}.")

    def devolver_livro(self, usuario, livro):
        if livro not in usuario.get_livros():
            print(f"{usuario.get_nome()} não possui esse livro.")
            return
          
        livro.set_disponivel(True)
        usuario.remover_livro(livro)
        print(f"Livro '{livro.get_titulo()}' devolvido por {usuario.get_nome()}.")


biblioteca = Biblioteca()

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")
livro3 = Livro("O Hobbit", "J.R.R. Tolkien")
livro4 = Livro("Python Básico", "Autor X")

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)
biblioteca.cadastrar_livro(livro4)

usuario = Usuario("Guilherme")

biblioteca.listar_livros()

biblioteca.emprestar_livro(usuario, livro1)
biblioteca.emprestar_livro(usuario, livro2)
biblioteca.emprestar_livro(usuario, livro3)

biblioteca.emprestar_livro(usuario, livro4)

biblioteca.emprestar_livro(usuario, livro1)

biblioteca.listar_livros()

biblioteca.devolver_livro(usuario, livro1)

biblioteca.devolver_livro(usuario, livro4)

biblioteca.listar_livros()
