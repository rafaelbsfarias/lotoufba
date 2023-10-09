# Crie um arquivo para armazenar as combinações
with open('todasCombinações.txt', 'w') as arquivo:
    # Insira todas as combinações possíveis
    for n1 in range(1, 12):
        for n2 in range(n1 + 1, 13):
            for n3 in range(n2 + 1, 14):
                for n4 in range(n3 + 1, 15):
                    for n5 in range(n4 + 1, 16):
                        for n6 in range(n5 + 1, 17):
                            for n7 in range(n6 + 1, 18):
                                for n8 in range(n7 + 1, 19):
                                    for n9 in range(n8 + 1, 20):
                                        for n10 in range(n9 + 1, 21):
                                            for n11 in range(n10 + 1, 22):
                                                for n12 in range(n11 + 1, 23):
                                                    for n13 in range(n12 + 1, 24):
                                                        for n14 in range(n13 + 1, 25):
                                                            for n15 in range(n14 + 1, 26):
                                                                # Escreva a combinação no arquivo
                                                                arquivo.write(f"{n1},{n2},{n3},{n4},{n5},{n6},{n7},{n8},{n9},{n10},{n11},{n12},{n13},{n14},{n15}\n")

print("Arquivo todasCombinações.txt criado com todas as combinações possíveis.")
