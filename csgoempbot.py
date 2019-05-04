from selenium import webdriver
import winsound
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = ''
website = 'https://csgoempire.com/#!'
browser = webdriver.Chrome(path)
browser.get(website)
# 30 sekund na zalogowanie sie.
timeOfBet = []
timeOfBalanceCheck = []
randomSecBet = randint(6, 9)
randomSecBalance = randint(10, 13)
for i in range(60):
    timeOfBet.append(str(randomSecBet) + "." + str(i))
for i in range(60):
    timeOfBalanceCheck.append(str(randomSecBalance) + "." + str(i))
time.sleep(45)
betCT = browser.find_element_by_class_name('ct')
betTT = browser.find_element_by_class_name('t')
betted = False
#
# Wartosci ustawiane przez uzytkownika
startingBetValue = 0.01
betLimit = 0.16
maxProfit = 0.10
#
#
loseTrain = 0
currentBet = startingBetValue
profit = 0
print("bot starting...")
botOn = True
while(botOn):
    betSite = randint(0, 40000)
    if (betSite % 2 == 0):
        betSite = betCT
    else:
        betSite = betTT
    if (currentBet > betLimit):
        frequency = 2500
        duration = 1000
        winsound.Beep(frequency, duration)
        print("Bot zakonczyl prace... Limit beta przekroczony")
        botOn = False
    if (profit >= maxProfit):
        frequency = 2500
        duration = 2000
        winsound.Beep(frequency, duration)
        print("Bot zakonczyl prace... \n Profit: " + str(round(profit, 2)))
        botOn = False
    timeToRoll = browser.find_element_by_class_name('rolling-overlay__time').text

    editor = browser.find_element_by_xpath('.//input[@type="number"][@class="c-input c-input--basic bet-amount"]')
    balanceBeforeBet = float(browser.find_element_by_xpath('.//span[@class = "u-hl-gold"]').text)
    # Bet za okreslona wartosc, jesli ostatni bet przegrany to 2x wiecej, jesli wygrany to wartosc poczatkowa
    # czyszczenie wartosci bet'a oraz wysylanie beta po sekundzie
    # czekanie az timetoroll bedzie wiekszy niz na poczatku
    print("pierwszy while dziala....")
    while (True):
        timeToRoll = browser.find_element_by_class_name('rolling-overlay__time').text
        if (timeToRoll in timeOfBet):
            editor.clear()
            break
    print("pierwszy while zakonczyl prace....")
    editor.send_keys(str(currentBet))
    time.sleep(1)
    print("Stawianie beta....")
    changeBet = randint(5, 8)
    print("random")
    betSite.click()
    betted = True
    timeToRoll = browser.find_element_by_class_name('rolling-overlay__time').text
    print("drugi while dziala....")
    while (True):
        timeToRoll = browser.find_element_by_class_name('rolling-overlay__time').text
        if (timeToRoll in timeOfBalanceCheck):
            balanceAfterBet = float(browser.find_element_by_xpath('.//span[@class = "u-hl-gold"]').text)
            if (balanceAfterBet > balanceBeforeBet):
                profit += startingBetValue
                currentBet = startingBetValue
                loseTrain = 0
                betted = False
                break
            elif (balanceAfterBet < balanceBeforeBet):
                currentBet = currentBet * 2
                betted = False
                loseTrain += 1
                break
            else:
                break
        continue
    print("drugi while zakonczyl prace...")
    print("profit= " + str(round(profit, 2)))
    continue
