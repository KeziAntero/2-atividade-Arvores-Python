class Arvore:
    valor = None 
    f_esq = None 
    f_dir = None
    
    def __init__(self,valor,f_esq=None,f_dir=None) :
        self.valor = valor 
        self.f_esq = f_esq 
        self.f_dir = f_dir

    def __str__(self) :
        return str(self.valor)



    def inserir(self, valor) : 
  
        if self.valor:
            if valor < self.valor:
                if self.f_esq is None:
                    self.f_esq = Arvore(valor)
                else:
                    self.f_esq.inserir(valor)
            elif valor > self.valor:
                if self.f_dir is None:
                    self.f_dir = Arvore(valor)
                else:
                    self.f_dir.inserir(valor)
        else:
            self.valor = valor

    def red(self):      
        if self:
            print(str(self.valor), end = ' ')
            if self.f_esq:
                self.f_esq.red()
            if self.f_dir:
                self.f_dir.red()


    def erd(self):        
        if self:
            if self.f_esq:
                self.f_esq.erd()
            print(str(self.valor), end = ' ')
            if self.f_dir:
                self.f_dir.erd()


root = Arvore(4)
root.inserir(2)
root.inserir(1)
root.inserir(3)
root.inserir(6)

#              4
#            /  \
#           2    6
#         /  \    
#       1     3  


print(root.erd())

print(root.red())



def altura(no) :
    if no is None:
        return 0;

    else :

        altura_esq = altura(no.f_esq) 
        altura_dir = altura(no.f_dir)
                
        if (altura_esq > altura_dir):
            return altura_esq+1
        else:
            return altura_dir+1
                   
print ("\nA altura da arvore e: %d" %(altura(root))) 
        


def buscar(no, valor):
    if no is None:
        print(f'{valor} nao foi encontrado na arvore')
        return
    if no.valor == valor:
        print(f'{valor} foi encontrado na arvore')
        return no
    if valor > no.valor:
        buscar(no.f_dir, valor)
    else:
        buscar(no.f_esq, valor)

if __name__ == '__main__':
    buscar(root, 7) 

         
def valorMin(no):
    noAtual = no
 
    
    while(noAtual.f_esq is not None):
        noAtual = noAtual.f_esq
 
    return noAtual
 
def remover(root, valor):  
    if root is None:
        return root
    if valor < root.valor:
        root.f_esq = remover(root.f_esq, valor)
    elif(valor > root.valor):
        root.f_dir = remover(root.f_dir, valor)
    else:
        if root.f_esq is None:
            temp = root.f_dir
            root = None
            return temp
 
        elif root.f_dir is None:
            temp = root.f_esq
            root = None
            return temp
        temp = valorMin(root.f_dir)
        root.valor = temp.valor
        root.f_dir = remover(root.f_dir, temp.valor)
    return root

    
print('\nRemover o num: 2')
root = remover(root, 2)


print(root.erd())

print(root.red())

print ("\nA altura da arvore agora e: %d" %(altura(root))) 

#              4
#            /  \
#           2    6
#         /  \    
#       1     3  

