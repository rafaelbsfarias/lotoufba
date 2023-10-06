## Dada uma sequencia de 13 números esse script gera uma sequencia de 15 números que somam entre
## 190 e 199, e nunca foi sorteado. 
import random

# Números pré-selecionados
pre_selected_numbers = [2, 5, 8, 10, 11, 13, 14, 15, 20, 21, 23, 24, 25]

# Função para verificar se a soma está entre 190 e 199
def is_valid_sequence(sequence):
    return 190 <= sum(sequence) <= 199

# Inicialize uma lista para rastrear as sequências geradas
sequencias_geradas = []

# Crie uma função para gerar uma sequência de 15 números não repetidos
def generate_sequence():
    while True:
        # Inicialize a sequência com os números pré-selecionados
        sequence = pre_selected_numbers.copy()
        
        # Enquanto a sequência não tiver 15 números
        while len(sequence) < 15:
            # Escolha aleatoriamente um número que não esteja na sequência
            random_number = random.randint(1, 25)
            
            while (random_number in sequence or random_number in pre_selected_numbers):
                random_number = random.randint(1, 25)
            
            # Adicione o número à sequência
            sequence.append(random_number)
        
        # Ordene os números em ordem crescente
        sequence.sort()
        
        # Verifique se a soma dos números está entre 190 e 199
        if is_valid_sequence(sequence) and sequence not in sequencias_geradas:
            sequencias_geradas.append(sequence)
            return sequence

# Gere 50 sequências de 15 números
for i in range(50):
    new_sequence = generate_sequence()
    
    # Exiba os 15 números selecionados
    print(f"Sequência gerada {i+1} de 15 números:")
    print(new_sequence)

    # Verifique se a sequência existe em resultadosAnteriores.txt
    with open('resultadosAnteriores.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        sequence_as_string = ','.join(map(str, new_sequence))
        
        if sequence_as_string in linhas:
            print("Esta sequência já existe em resultadosAnteriores.txt.")
        else:
            print("")
            #print("Esta sequência não existe em resultadosAnteriores.txt.")
