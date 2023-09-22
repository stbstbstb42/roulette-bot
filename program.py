import time
from datetime import datetime

# nome del file
nome_file = "reports/" + time.asctime(time.localtime()).replace(' ', '-').replace(':', '.') + ".txt"

fileSessione = "reports/" + time.asctime(time.localtime()).replace(' ', '-').replace(':', '.')
nome_file =  fileSessione + ".txt"
with open(nome_file, 'w') as file:
    file.write('')
file.close()
    
nowDate = datetime.now()
strr = str(str(nowDate.hour) + ":" + str(nowDate.minute) + ":" + str(nowDate.second) + '\n')

# salva in txt sessione
with open(nome_file, 'a') as file:
    file.write(str(strr))
file.close()