#https://v2.jokeapi.dev/joke/Any?type=single
import os
import jokehandler

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n-Förläng livet med en torr historia-")

    url = f"https://v2.jokeapi.dev/joke/Any?type=single"

    nr = 1
    jokeobjekt = jokehandler.Jokehandler(url)

    while True:

        t_joke = jokeobjekt.get_joke()

        print(f"\n{nr}.------------------------")
        print(f"{t_joke}")
        print("----------------------------------\n")



        nr += 1

        entill = input("Vill du ha ett till skämt? J/N")

        if (entill == "n" or entill == "N"):
            break

main()