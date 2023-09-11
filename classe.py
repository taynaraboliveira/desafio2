class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0.0
        self.limite_velocidade = 180.0

    def liga(self):
        self.ligado = True

    def desliga(self):
        self.velocidade = 0.0
        self.ligado = False

    def acelera(self):
        if not self.ligado:
            return

        if self.velocidade < self.limite_velocidade:
            self.velocidade += 5

    def desacelera(self):
        if not self.ligado:
            return

        if self.velocidade > 0:
            self.velocidade -= 5

    def __str__(self):
        ligado_str = "ligado" if self.ligado else "desligado"
        return f"Carro {self.modelo} da cor {self.cor} está {ligado_str}, à velocidade de {self.velocidade} km/h."

# Cria uma instância da classe Carro
carro = Carro(cor="vermelho", modelo="gol")
print(carro)

# Liga o carro
carro.liga()
print(carro)

# Acelera o carro
carro.acelera()
print(carro)

# Desacelera o carro
carro.desacelera()
print(carro)

for _ in range(5):
    carro.acelera()

# Desliga o carro
carro.desliga()
print(carro)
