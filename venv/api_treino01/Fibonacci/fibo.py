class Fibonacci:
    def __init__(self, numero, fibo = []):
        self.numero = numero
        self.fibo = fibo
    def calc_fibo(self):
        if self.numero == 1:
            self.fibo.append(1)
            return self.fibo
        if self.numero == 2:
            self.fibo.append(1)
            self.fibo.append(1)
            return self.fibo
        
        if self.numero > 2:
            atual = 1
            anterior = 1
            self.fibo = [1,1]
            for i in range(2,self.numero):
                soma = atual + anterior
                self.fibo.append(soma)
                atual = anterior
                anterior = soma
            return self.fibo

if __name__ == '__main__':
    fibo = Fibonacci(10)

    print(fibo.calc_fibo())
                
                
            


