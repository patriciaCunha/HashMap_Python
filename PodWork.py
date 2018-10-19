class HashMap:
    def __init__(self):
        self.size= 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
    
    def put(self, name, user):
        key_hash = self._get_hash(name)

        if self.map[key_hash] is None:
            self.map[key_hash] = [user]
        else:
            for pair in self.map[key_hash]:
                if pair.name == name:
                    pair = user
                    return True
            self.map[key_hash].append(user)

    def get(self, name):
        key_hash = self._get_hash(name)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair.name == name:
                    return pair
        return None 
    
    def Contains(self, name):
        contain = self.get(name)
        if contain is not None:
            return True
        return False
    
    def printar(self):
        print("--------USUARIOS--------")
        for user in self.map:
            if user is not None:
                for users in user:
                    print ("Nome: "+users.name+", Altura: " + str(users.height)+ "\n")
    
    def count(self):
        count = 0
        posicao = 1
        for size in self.map:
            if size is not None:
                sizeEmCada = 0
                for cadaSize in size:
                    sizeEmCada = sizeEmCada + 1
                    count = count + 1
                print("No " + str(posicao) + ", possui " +  str(sizeEmCada))
            posicao = posicao + 1
        print("Tem no total " + str(count))

class User:
    def __init__(self, name, height):
        self.name = name
        self.height = height

from random import *
class GerarUser:
    def __init__(self):
        self.name= ""
        self.height = 0
        self.consoante=["b","c","d","f","g","h","j","k","l","m","n"
             ,"p","q","r","s","t","v","w","x","y","z"]

        self.vogal = ["a","e","i","o","u"]

    def gerarNome(self):
        size = randint(3,18)
        posicao = randint(0,1)

        if posicao == 0:
            for i in range(size + 1,1, -1): 
                if i%2 == 0:
                    posicao = randint(0, len(self.consoante) - 1)
                    self.name = self.name + self.consoante[posicao]

                else:            
                    posicao = randint(0, len(self.vogal) - 1)
                    self.name = self.name + self.vogal[posicao]
        else:
            for i in range(size + 1,1, -1): 
                if i%2 == 0:
                    posicao = randint(0, len(self.vogal) - 1)
                    self.name = self.name + self.vogal[posicao]

                else:            
                    posicao = randint(0, len(self.consoante) - 1)
                    self.name = self.name + self.consoante[posicao]
                    
        return self.name
        

    def gerarAltura(self):
        height = randint(90,200)
        self.height = height/100
        return self.height

    def gerarUser(self):
        user = User(self.gerarNome() , self.gerarAltura())
        #print(self.name)
        return user




     

if __name__ == "__main__":

    h = HashMap()
    while True:
        print ("1 - Inserir Usuário\n")
        print ("2 - Pesquisar Usuário\n")
        print ("3 - Buscar Usuário\n")
        print ("4 - Quantidade no hash\n")
        print ("5 - Sair\n")

        opcao = input("Digite a sua Opção:\n")

        if opcao == "1":
            qtdInserir = int(input("Quantos usuários você deseja inserir?\n"))
            for i in range(0,qtdInserir):
                user = GerarUser()
                usuario = user.gerarUser()
                h.put(usuario.name, usuario)
                print(user.name)
            print("Parabéns! Dados inseridos com sucesso!")    
        
        elif opcao == "2":
            pesquisar = input("Qual o usuário deseja pesquisar?\n")
            result = h.Contains(pesquisar)
            if result:
                print("Usuário encontrado")
            else:
                print("Usuário não encontrado")

        elif opcao == "3":
            busca = input("Qual usuário deseja buscar?\n")
            result = h.get(busca)
            if result is not None:
                print("Nome é " + result.name + "e a altura é " + str(result.height))
            else:
                print("Registro não encontrado")    

        elif opcao == "4":
            h.count()   

        elif opcao == "5":
            print("Tchau! Até a próxima!:D Glória à Deuxxx")
            break;
