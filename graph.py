import matplotlib.pyplot as plt

fileSessione = "reports/Wed-Mar-22-12.46.49-2023/session1"
nome_file =  fileSessione + ".txt"
dati = [line.strip().split() for line in open(nome_file, 'r')]
x = [float(riga[0]) for riga in dati]
y = [float(riga[1]) for riga in dati]
labels = [riga[2] if len(riga) >= 3 else '' for riga in dati]  # controlla se ci sono almeno tre elementi nella riga
plt.figure(figsize=(20, 10))
plt.plot(x, y)
plt.grid()
plt.xlabel('Time')
plt.ylabel('Balance')
plt.xticks(x, ['']*len(x))  # imposta le etichette sull'asse x come spazi vuoti
for label, x_pos, y_pos in zip(labels, x, y):
    plt.annotate(label, xy=(x_pos, y_pos), xytext=(5, 5), textcoords='offset points', ha='left', va='bottom')
plt.figtext(0.95, 0.05, ("FAILED"), ha='right', va='bottom')
plt.xlim(x[0], x[-1])
plt.savefig(fileSessione + ".png")