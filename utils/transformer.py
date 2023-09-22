with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
    for line in input_file:
        data = line.strip().split() # separa la riga in base agli spazi
        number = data[2] # estrae il numero dalla terza posizione
        output_file.write(number + "\n") # scrive il numero su una nuova riga nel file di output
