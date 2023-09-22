"""
roulette-bot v0.1
"""

#1350, 1020

from defs import *
import random
import pyautogui
import os
import time
import pyperclip
import matplotlib.pyplot as plt
from datetime import datetime
from sites import *
from id import *


def main():
    # Incogniton open
    
    #methods
    ifsix = 0
    
    # Configuration
    
    sessionGain = int(input("Session target: "))
    print(sessionGain)
    gain = int(input("Site target: "))
    rOrb = str(input("Red (r) or Black (b)? "))
    bet = int(input("Insert the coin: (1 = 0.50)"))
    

    startBalance = 0
    graphicI = 0 

    # session txt
    
    reportPath = "reports/" + time.asctime(time.localtime()).replace(' ', '-').replace(':', '.')
    os.makedirs(reportPath)
    
    
    # insert balance in txt
    

    input("Press Enter to START!")
    
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    pyautogui.click(710, 20) # browser click
    #click(closeAccount)
    #move2Tab()
    
    print("Script STARTED")
    # print("\nStarting from: " + str(startBalance) + "\n")
    
    # Start!!
    balance = startBalance
    
    # init variables
    fail = 0 # number of failures
    
    fatalErrNum = 0
    
    lastResult = 0 # save last result
    lastResultError = False
    negBalance = 0
    
    lastWinBalance = 0
    loseMoltiplier = 0
    
    sessionTime = time.time() # to return total session time
    startedHour = str(datetime.now().hour)
    startedMinute = str(datetime.now().minute)
    startedSecond = str(datetime.now().minute)
    
    sessionBalance = 0.0
    
    lastWinBalance = startBalance
    fail = 0
    balance = 0
    i = 0
    lastChosenSite = str
    lastChosenProvider = str
    lastChosenRoul = str
    sessionID = 0
    # start session
    while int(sessionBalance) < sessionGain:
        
        # random site and provider and settings
        selected_site_name = random.choice(list(sites.keys()))
        
        """
        while (selected_site_name) == lastChosenSite:
            selected_site_name = random.choice(list(sites.keys()))

        lastChosenSite = selected_site_name
        """
        if rOrb == 'b':
            lastSpin = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["bet"]
            reverseSpin = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["reverseBet"]
        elif rOrb == 'r':
            lastSpin = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["reverseBet"]
            reverseSpin = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["bet"]
        #reverseSpin = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["reverseBet"]
        cameraView = sites[selected_site_name]["providers"]["pragmaticPlay"]["buttons"]["cameraView"]
        balancePos = sites[selected_site_name]["buttons"]["balancePos"]
        account = sites[selected_site_name]["buttons"]["account"]
        closeAccount = sites[selected_site_name]["buttons"]["closeAccount"]
        all_providers = sites[selected_site_name]["providers"]
        
        
        
        pyautogui.hotkey('ctrl', 'l')
        wait(0.2)
        pyautogui.write(sites[selected_site_name]["mainLink"])
        pyautogui.press('enter')
        wait(10)
        
        click(account)
        wait(7)
        balance = getBalance(balancePos)
        wait(1)
        click(closeAccount)
        wait(1)
        siteBalance = balance
        veryFirstBal = startBalance
        
        minBalance = balance
        maxBalance = balance
        sessionID = sessionID + 1
        nome_file = reportPath + "/session" + str(sessionID) + ".txt"
        with open(nome_file, 'w') as file:
            file.write('')
        file.close()
        
        os.makedirs(reportPath + "/bets_screens/" + str(sessionID))
        
        
        saveToTxt(nome_file, graphicI, balance, startBalance, gain)
        
        
        
        betNbr = 1
        
        while int(balance) < siteBalance + gain: # site loop 
            
            fatalError = 0 # fatal error restart
            firstShowBal = True
            firstShowBalError = 0
            # check if the first tab is the right home (debug from an error)
            
            #choose provider
            selected_provider = random.choice(list(all_providers.keys()))
            
            """
            while (selected_provider == lastChosenProvider):
                selected_provider = random.choice(list(all_providers.keys()))
            
            lastChosenProvider = selected_provider
            """
            
            # ocr&buttons posx, posy
            ocr_pos = sites[selected_site_name]["providers"][selected_provider]["ocrs"]
            
            # choose roulette-site
            roulette_path = sites[selected_site_name]["providers"][selected_provider]["links"]
            roulette_site = random.choice(list(roulette_path.keys()))
            
            
            while (lastChosenRoul == roulette_site):
                roulette_site = random.choice(list(roulette_path.keys()))
            lastChosenRoul = roulette_site
            
            pyautogui.hotkey('ctrl', 't')
            wait(0.2)

            


            pyautogui.write(roulette_path[roulette_site])


            wait(0.2)
            pyautogui.press('enter')
            oldtime = time.time()
            
            
            while (goSpin(ocr_pos["firstCheck"]["x1"], ocr_pos["firstCheck"]["y1"], ocr_pos["firstCheck"]["x2"], ocr_pos["firstCheck"]["y2"]).find("R") == -1 and fatalError != 1):
                if time.time() - oldtime > 89:
                    fatalError = 1
                else:
                    wait(0.2)
            
            wait(2)
            click(cameraView)
            
            roundTime = time.time() # start round time
            errorRestart = 0
            youWon = 0
            roundBalance = balance
            
            # single round loop 
            # while (balance < roundBalance + (bet / 2)) and (balance > roundBalance - ((bet / 2) * 5)) and (time.time() - roundTime < 1800) and (int(balance) < (balance + gain)) and (errorRestart == 0 and fatalError != 1):
            while (balance < roundBalance + 5) and (balance > roundBalance - 5) and (time.time() - roundTime < 1800) and (int(balance) < (balance + gain)) and (errorRestart == 0 and fatalError != 1):
                # restart balance
                prevBalance = balance 
                
                # check if errors
                oldtime = time.time() # start time for error
                while (checkNumbers(ocr_pos["secondCheck"]["x1"], ocr_pos["secondCheck"]["y1"], ocr_pos["secondCheck"]["x2"], ocr_pos["secondCheck"]["y2"]).find("1") == -1) and errorRestart == 0:
                    if time.time() - oldtime > 89:
                        errorRestart = 1
                    else:
                        wait(0.1)
                print("Second Check Done!")
                oldtime = time.time() # restart time
                # check if begin bet (from chat) + recheck error 
                while (goSpin(ocr_pos["thirdCheck"]["x1"], ocr_pos["thirdCheck"]["y1"], ocr_pos["thirdCheck"]["x2"], ocr_pos["thirdCheck"]["y2"]).find('e') == -1) and errorRestart == 0:
                    if time.time() - oldtime > 89:
                        errorRestart = 1
                    else:
                        wait (0.1)
                print("Third Check Done!")        
                if firstShowBalError == 2:
                    errorRestart = 1
                
                if (errorRestart == 0): # check if no errors
                    wait(0.2)
                    if selected_site_name != "betano":
                        move1Tab()
                        wait(1)
                        click(account)
                        wait(1)
                    elif selected_site_name == "betano":
                        wait(4)
                        click(account)
                        wait(4)
                        
                    balance = getBalance(balancePos)
                    if balance > maxBalance:
                            maxBalance = balance
                    elif balance < minBalance:
                            minBalance = balance
                    
                    if balance != prevBalance:
                        graphicI = graphicI + 1
                        saveToTxt(nome_file, graphicI, balance, startBalance, gain)
                    
                    wait(0.2)
                    click(closeAccount)
                    wait(0.2)
                    
                    move2Tab()
                    wait(0.8)
                    
                    if (balance > prevBalance):
                        print("\nCongrats, U WON!")
                        fail = 0 
                        lastResult = 1
                        lastResultError = False
                        negBalance = 0
                        lastWinBalance = balance
                        firstShowBal == False
                        youWon = 1
                        sessionBalance = sessionBalance + (balance - prevBalance)
                        if balance >= maxBalance:
                            loseMoltiplier = 0
                        
                    elif (balance < prevBalance):
                        print("\nFAILED :(")
                        negBalance = negBalance + (prevBalance - balance)
                        fail = fail + 1
                        lastResult = 0
                        lastResultError = False
                        firstShowBal == False
                        assurance = lastWinBalance - balance
                        lastWinBalance = balance
                        sessionBalance = sessionBalance - (prevBalance - balance)
                        loseMoltiplier = loseMoltiplier + 1
                        print("Failures: " + str(fail))
                        
                        
                        tmp = lastSpin
                        lastSpin = reverseSpin
                        reverseSpin = tmp
                        
                    elif (firstShowBal == True):
                        print("Round starting from:")
                        firstShowBalError = firstShowBalError + 1
                        lastResultError = False
                    else:
                        print("Oh oh, something went wrong during balance reporting!")
                        lastResultError = True
                    
                    print("Balance: " + str(balance))
                    print(bet)
                    print(time.asctime(time.localtime()))
                    #if balance != (balance + gain) and (balance < roundBalance + (bet / 2)) and (balance > roundBalance - ((bet / 2) * 5)):
                    if balance != (balance + gain) and (balance < roundBalance + 5) and (balance > roundBalance - 5):
                        wait(1.5)
                        pyautogui.click(lastSpin, clicks=bet, interval=0.1)
                        pyautogui.screenshot(reportPath + "/bets_screens/" + str(sessionID) + '/' + str(graphicI) + ".jpeg")
                        wait(20)
            move2Tab()
            wait(0.4)
            pyautogui.hotkey('ctrl', 'w')
            if fail == 2:
                print(str(i + 1) + "Round failed, RETRY\n" + "Closed with loss: " + str(balance - siteBalance))
                print("Min Balance: " + str(minBalance) + "\nMax Balance: " + str(maxBalance) + "\n")
                print(str(i + 2) + " Round STARTS!\n")
            elif errorRestart == 1:
                print(str(i + 1) + " Round failed for error, RESTART\n")
                print(str(i + 2) + " Round STARTS!\n")
            elif fatalError == 1:
                print("FATAL ERROR!")
            else:
                print(str(i + 1) + " Round DONE!\n" + "Closed with balance: " + str(balance - siteBalance))
                print("Min Balance: " + str(minBalance) + "\nMax Balance: " + str(maxBalance) + "\n")
                print(str(i + 2) + " Round STARTS!\n")
            fail = 0
            i = i + 1
            startBalance = balance
            wait(random.randint(4, 7))
        print("Completed Site\nStarted from: " + str(veryFirstBal) + "\nFinished at: " + str(sessionBalance))
        print ("Time: " + str(str(int((int(time.time())) - int(sessionTime)) / 60) + " minutes and " + str(int(time.time()) - int(sessionTime)) + " seconds"))
        print("Fatal Errors Resolved: " + str(fatalErrNum))
        
        # crea grafico
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
        plt.figtext(0.95, 0.05, ("Started at: " + startedHour + ':' + startedMinute + ':' + startedSecond + "\nFinished at: " + str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' + str(datetime.now().second)), ha='right', va='bottom')
        plt.xlim(x[0], x[-1])
        plt.savefig(reportPath + "/graph" + str(sessionID + 1) + ".png")
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    """
    dir_path = "G:/My Drive/asd"
            computer_id = 'a'

            # Leggi l'ultimo link aperto dagli altri computer
            other_links = []
            for file_name in os.listdir(dir_path):
                if file_name.endswith('.txt') and file_name != computer_id + '.txt':
                    with open(os.path.join(dir_path, file_name), 'r') as f:
                        last_link = f.readlines()[-1].strip()
                        if last_link in globals():
                            last_link = globals()[last_link]
                            other_links.append(last_link)

            # Sposta l'URL di Azure nella posizione 2 se è stato aperto su un altro computer
            if last_link in other_links:
                posizione = linkList.index(last_link)
                temp = linkList[6]
                linkList[6] = linkList[posizione]
                linkList[posizione] = temp
                
                
                
            after choosing site
            for var_name, var_val in locals().items():
                if var_val == link_to_open:
                    with open(os.path.join(dir_path, computer_id + '.txt'), 'w') as f:
                        f.write(link_to_open + '\n')
    """