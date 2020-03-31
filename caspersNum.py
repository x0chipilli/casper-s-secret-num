import random
import os
import time

def getCaspersNum():
  return random.randint(1,100)

def getTry():
  while True:
    uTry = input('--GueSs tHe nUm8eR ((1 - 1OO))::: ')

    if not isNumber(uTry):
      print('brah just type a NUMBER ok ᕙ(⇀‸↼‶)ᕗ')
    elif uTry == '':
      print('at leAst type sumThin y0 -.-')
    elif (int(uTry) < 0 or int(uTry) > 100):
      print("dude, my bro casper's num is between 0-100 ๏_๏")
    else:
      return int(uTry)
    
def isNumber(input):
  for i in input:
    if i not in '0123456789':
      return False

  return True

def getHint(uTry, casperNum):
  if uTry < casperNum:
    print('  .-""""-.')
    print(" / -   -  \'")
    print('|  .-. .- |')
    print('|  \o| |o (')
    print('\     ^    \'')
    print(" '.  )--'  /   CaspEr saYz:::")
    print("   '-...-'`    ma num iS biGgER")
    print()
  elif uTry > casperNum:
    print('  .-""""-.')
    print(" / -   -  \'")
    print('|  .-. .- |')
    print('|  \o| |o (')
    print('\     ^    \'')
    print(" '.  )--'  /   CaspEr saYz:::")
    print("   '-...-'`    ma num iS sHorta")
    print()
  elif uTry == casperNum:
    print('  .-""""-.')
    print(" / -   -  \'")
    print('|  .-. .- |')
    print('|  \o| |o (')
    print('\     ^    \'')
    print(" '.  )O'   /   CaspEr saYz:::")
    print("   '-...-'`    brO thats actuaLLy ma nuM")
    print()

def playAgain():
  return input('plAy agAiN?? ((y/n))::: ').lower().startswith('y')

def chooseDifficulty():
  print('-----gAme mo0des-----')
  print('1 === eAsy PeaCy')
  print('2 === neUtral')
  print('3 === imPossIble')
  print()

  while True:
    difficulty = input('cho0se moDe::: ')

    if difficulty not in '123':
      print('bro, just 3 optiOns that\'s what it is ¯\(©¿©) /¯')
    elif len(difficulty) != 1:
      print('man just cHoOse 1 of theSe u.U')
    else:
      os.system('clear')
      return difficulty

def getAttempts():
  option = chooseDifficulty()

  if option == '1':
    return 20
  elif option == '2':
    return 10 
  elif option == '3':
    return 5



print('..-**+"-- C A S P e R \'s  N U M --"+**-..')
print()
casperNum = getCaspersNum()
maxAttempts = getAttempts()
attempt = 1

while True:
  while attempt <= maxAttempts:
    uTry = getTry()
    getHint(uTry, casperNum)

    if uTry == casperNum:
      break
    else:
      attempt += 1
      input()
      os.system('clear')
  
  if attempt == maxAttempts + 1:
    print('u uSe aLL of youR attempts dUmbAsss (¬_¬)')
    print()
  else:
    print('conGraTz!! u guEss casPer\'s num in just %s attEmpTs!! uve won nuUthin!!!!! ヽ(^◇^*)/'%(attempt))
    print()


  if playAgain():
    os.system('clear')
    casperNum = getCaspersNum()
    maxAttempts = getAttempts()
    attempt = 1
  else:
    os.system('clear')
    print('bye byE ✿◕ ‿ ◕✿')
    time.sleep(2)
    break