'''''''--------------- aluno.py ------------------'''
import uuid

class Pessoa:
    def __init__(self, nome, idade):
        # uuid => gera um identificador único de 36 caracteres --> identificador universal
        self.matricula = uuid.uuid1() #função que gera matricula aleatória.
        self.nome = nome
        self.idade = idade
class Aluno(Pessoa): # classe que está herdando de Pessoa. Par
    def __init__(self, nome, idade, curso, nota):
        super().__init__(nome, idade)
        self.curso = curso
        self.nota = nota
    def __repr__(self):# função reprodução. Se colocar isso nao vai printar somente o endereço de memória.
        return f'Matricula: {self.matricula} \n' \
               f'Nome: {self.nome} \n' \
               f'Idade: {self.idade} \n' \
               f'Curso: {self.curso} \n' \
               f'Nota: {self.nota}'

if __name__ == "__main__":
    aluno = Aluno("Jonas", 17, "Python", 9.5)
    print(aluno) #vai printar o endereço de memoria;