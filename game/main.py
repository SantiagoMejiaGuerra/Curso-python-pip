import random

def choice_options():
    options = ("piedra", "papel", "tijera")
    user = input("Elija piedra, papel o tijera --> ")
    user = user.lower()
    #Eligira de forma aleatoria la opcion 

    if not user in options:
        print("esa opcion no es valida")
        #continue
        return None, None

    Computer = random.choice(options)

    print("User options-->", user)
    print("Computer options-->", Computer)
    return user, Computer

def check_rules(user, Computer, user_wins, computer_wins):
    if user == Computer:
        print("Empate")
    elif user =="piedra" :
        if Computer == "tijera":
            print("Piedra gana a tijera")
            print ("Ganaste")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("Computer gano")
            computer_wins +=1
    elif  user == "papel":
        if Computer== "piedra":
            print("papel gana a piedra")
            print("user gano")
            user_wins += 1
        else:
            print("Tijera gana a papel")
            print("computer gano")
            computer_wins +=1
    elif  user == "tijera":
        if Computer== "papel":
            print("tijera gana a papel")
            print("ganaste")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print ("Computer gano")
            computer_wins +=1
    return user_wins, computer_wins

def run_game():
    user_wins=0
    computer_wins=0 
    rondas= 1
    while True:

        print("*" * 10 )
        print("Round",  rondas)
        print ("*" * 10)

        print("User -->", user_wins)
        print("Computer -->", computer_wins)

        rondas = rondas + 1 

        user, Computer = choice_options()
        user_wins, computer_wins = check_rules(user, Computer, user_wins, computer_wins)

        if computer_wins == 2:
            print ("El ganador es la computadora")
            break
        if user_wins == 2:
            print ("El ganador es el usuario")
            break

run_game()