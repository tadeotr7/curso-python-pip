import random

def get_user_choice():
    """Obtiene la elección del usuario y la valida."""
    while True:
        choice = input('''Elije entre:
        1) Piedra
        2) Papel
        3) Tijeras
        (Introduce el número de tu elección): ''')
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Esa no es una jugada válida. Inténtalo de nuevo.")

def determine_winner(user_choice, computer_choice):
    """Determina el ganador de la ronda."""
    print("El usuario eligió:", user_choice)
    print("La computadora eligió:", computer_choice)

    if user_choice == computer_choice:
        print("Es un empate!")
    elif (user_choice == "Piedra" and computer_choice == "Tijeras") or \
         (user_choice == "Papel" and computer_choice == "Piedra") or \
         (user_choice == "Tijeras" and computer_choice == "Papel"):
        print("Felicidades, usted ha ganado!")
    else:
        print("La computadora ha ganado!")

def game_logic():
    """Lógica principal del juego."""
    options = {"1": "Piedra", "2": "Papel", "3": "Tijeras"}
    user_choice = options[get_user_choice()]
    computer_choice = random.choice(list(options.values())) 
    determine_winner(user_choice, computer_choice)

if __name__ == "__main__":
    print("Hola desde mi MAC m1") 
    game_logic()
