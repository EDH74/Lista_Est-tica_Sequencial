class Les():
    def __init__ (self, tamanho):
        self.tam = tamanho
        self.quantidade = 0
        self.vetor = [None] * self.tam
        
    
    def inserir_fim(self, val):
        if self.esta_cheia():
            print("Lista está cheia")
        else:
            self.vetor[self.quantidade] = val
            self.quantidade += 1

    def remover_fim(self):  
        if self.quantidade != 0:
            self.quantidade -=1

    
    def esta_cheia(self):
        return self.quantidade >= self.tam
    
    def esta_vazia(self):
        return self.quantidade == 0
    
    def inserir_inicio(self, val):
        for i in range(self.quantidade, 0, -1):
            self.vetor[i] = self.vetor[i-1]
        self.vetor[0] = val
        self.quantidade +=1 
        
    def remover_inicio(self):
        for i in range(0, self.quantidade -1):
            self.vetor[i] = self.vetor[i+1]
        
        self.quantidade -=1
    
    def show(self):
        for i in range(0, self.quantidade):
            print(self.vetor[i], end=" ")
        print()
    
    def get_prim(self):
        return self.vetor[0]
    
    def get_ult(self):
        return self.vetor[self.quantidade]
    
    def get_quant(self):
        return self.quantidade
    
    def get_capacidade(self):
        return self.tam
    
    def remover(self, valor):
        for i in range(self.quantidade):
            if self.vetor[i] == valor:
                for e in range(i, self.quantidade -1):
                    self.vetor[e] = self.vetor[e+1]
        self.quantidade -= 1
            
                
    def index(self, valor):
        for i in range(0, self.quantidade):
            if self.vetor[i] == valor:
                return i
        return -1
    
    def existe(self, val):
        for i in self.vetor:
            if i == val:
                return True
        return False
    
    def remover_anterior(self, val):
        for i in range(self.quantidade-1, 0, -1):
            if self.vetor[i] == val:
                self.quantidade -=1
                for e in range(0, self.quantidade):
                    self.vetor[e] = self.vetor[e+1]
        
        
    def remover_posterior(self, val):
        for i in range(0, self.quantidade):
            if self.vetor[i] == val:
                for e in range(i, self.quantidade-1):
                    self.quantidade -=1
                    
    def remover_intervalo(self, val1, val2):
            for i in range(self.quantidade-1, 0, -1):
                if self.vetor[i] == val:
                    self.quantidade -=1
                    for e in range(0, self.quantidade):
                        self.vetor[e] = self.vetor[e+1]
                
                
    
    def show_inverso(self):
        for i in range(self.quantidade, 0, -1):
            print(self.vetor[i-1], end=" ")
        print()
    
    def inserir_apos(self, val1, val2):
        if self.quantidade > self.tam:
            for i in range(0, self.quantidade):
                if self.vetor[i] == val2 and i+1 != self.tam:
                    self.vetor[i] = val1
                
        else:
            print(val1, val2)
            for i in range(0, self.quantidade-1):
                if self.vetor[i] == val2:
                    self.vetor[i+1] = val1
                    
    def inserir_antes(self, val1, val2):
        if self.quantidade > self.tam:
            for i in range(0, self.quantidade-1):
                if self.vetor[i] == val2 and i+1 != self.tam:
                    self.vetor[i] = val1
                
        else:
            print(val1, val2)
            for i in range(0, self.quantidade):
                print(i)
                if self.vetor[i] == val2:
                    self.vetor[i-1] = val1
                    
    def get_valor(self, indice):
        if indice > self.tam:
            return False
        else:
            return self.vetor[indice]
        
    def limpar(self):
        self.quantidade = 0

    def contar_maiores(self, val):
        maiores = []
        for i in range(0, self.quantidade):
            if self.vetor[i] > val:
                maiores.append(self.vetor[i])
        
        return len(maiores)
    
    def trocar(self, indice1, indice2):
        temp = self.vetor[indice1]
        self.vetor[indice1] = self.vetor[indice2]
        self.vetor[indice2] = temp
                
    
    def inverter(self):
        self.vetor.reverse()
        
                