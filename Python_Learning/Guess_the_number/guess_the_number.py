import random
import os
import math
import time
history = [] 
playagain ="y"
while playagain == "y":
    os.system("cls" if os.name == "nt" else "clear")
    print("Starting new game...")
    
    #Numbers
    numbers=0
    while numbers<=0:
        try:
            print("How many numbers do you want")
            numbers=int(input())
            if numbers<=0:
                print("Invalid number")
                time.sleep(2)
                continue
        except ValueError:
            print("❌ Please enter a valid integer")
            time.sleep(2)
            continue

    
    secret= random.randint(1,numbers)
    
    #Tries
    max_tries=0
    tries=0 
   
   
    while max_tries<=0:
        try:
            print("How many tries do you want?")
            max_tries = int(input())
            if max_tries<=0:
                print("Invalid number of tries")
                time.sleep(2)
                continue
        except ValueError:
            print("❌ Please enter a valid integer")
            time.sleep(2)
            continue


        
    # === Dificultad con log2 ===
    needed = math.ceil(math.log2(numbers)) if numbers > 1 else 1
    # Clasificación (ajusta los cortes si quieres afinar)
    if max_tries >= needed + 2:
        difficulty = "Super Easy"
    elif max_tries == needed + 1:
        difficulty = "Easy"
    elif max_tries == needed:
        difficulty = "Medium"
    else:  # max_tries < needed
        difficulty = "Hard"

    print(f"You selected {numbers} numbers and {max_tries} tries")
    print(f"(theoretical min = {needed})")
    print(f"Difficulty: {difficulty}")
    
    print(f"Guess the number (1..{numbers})")
    result = "LOSE"  # por defecto es perder
    while tries<max_tries:
        print(f"You have {(max_tries)-tries} tries left")
        

        try:
            guess=int(input("Your guess: "))
        except ValueError:
            print("❌ Please enter a valid integer")
            time.sleep(2)
            continue
        if guess<=0 or guess>numbers:
            print (f"Invalid number, you must select a number between 1 and {numbers}")
            continue
        tries+=1
        if guess==secret:
            print("Correct")
            print(f"You guessed it in {tries} tries")
            result = "WIN"
            time.sleep(2)

            break
        elif guess>secret:
            print("Too high")
            
        elif guess<secret:
            print("Too low")
            
        
    else:
        print("Game over")
        print(f"Secret number was {secret}")
        time.sleep(2)
    # Guardar los datos de la partida
    history.append({
    "numbers": numbers,         # cantidad de números
    "max_tries": max_tries,     # intentos totales que tenía
    "used": tries,              # intentos usados
    "difficulty": difficulty,   # dificultad calculada
    "result": result            # WIN o LOSE
    })
    while True:
        

        print("Want to play again y/n")
        playagain=input().lower()
        if playagain=="y":
            break
        elif playagain=="n":
            print("Goodbye")
            break
        elif playagain not in ("y","n"):
            print("Invalid answer")
            time.sleep(2)


os.system("cls" if os.name == "nt" else "clear")
print("=== Session Summary ===")
for i, game in enumerate(history, 1):
    print(f"{i}. {game['result']} | Numbers={game['numbers']} | "
          f"Used {game['used']}/{game['max_tries']} tries | "
          f"Difficulty={game['difficulty']}")

print("Goodbye 👋")
time.sleep(5)

