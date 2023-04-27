carro_velocidade = 110
caminhao_velocidade = 80
distancia = 100


tempo_carro = distancia / carro_velocidade # Para descobrir o tempo que o carro vai percorrer
tempo_caminhao = distancia / caminhao_velocidade # Para descobrir o tempo que o caminhão vai percorrer
tempo_caminhao = tempo_caminhao + 10 # Adicionar a parada no pedagio para o caminhão, pois o carro tem sem parar

if tempo_carro < tempo_caminhao: # Se o tempo do carro for menor do que o caminhão, o carro chega mais rápido.
    print("Quem estará mais próximo de Ribeirão preto será o carro ")
else:
    print("Quem estará mais próximo de Ribeirão preto será o caminhão")
