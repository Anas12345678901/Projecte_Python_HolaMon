
Pelicules={
    "Gladiator": 15,
    "El lobo de Wall Street": 7,
    "Atrapame si puedes": 9,
    "La terminal": 11
}
def Mostrar_pelicules():
    print("\nPel·lícules disponibles:")
    for Pelicula in Pelicules:
        print(f"{Pelicula}")
def Reservar_entrades(Pelicula, Quantitat):
    if Pelicula in Pelicules:
        if Pelicules[Pelicula]>=Quantitat:
            Pelicules[Pelicula]-=Quantitat
            print(f"Operació completada amb exit{Quantitat} entrades per a {Pelicula}.")
        else:
            print("No hi ha entrades disponibles.")
    else:
        print("Aquesta pel·lícula no està disponible.")
def Mostrar_reserves():
    print("\nReserves:")
    for Pelicula, Disponibles in Pelicules.items():
        print(f"{Pelicula}: {Disponibles} entrades disponibles")
while True:
    print("1.Mostrar pel·lícules")
    print("2.Reservar entrades")
    print("3.Mostrar estat de les reserves")
    print("4.Sortir")
    Opció=input("Selecciona una opció")
    if Opció=="1":
        Mostrar_pelicules()
    elif Opció=="2":
        Pelicula=input("Introdueix el nom de la pel·lícula: ")
        try:
            Quantitat=int(input("Introdueix la quantitat de entrades a reservar:"))
            Reservar_entrades(Pelicula, Quantitat)
        except ValueError:
            print("Si us plau, introdueix un nombre vàlid.")
    elif Opció=="3":
        Mostrar_reserves()
    elif Opció=="4":
        print("Gràcies per utilitzar el sistema de reserves. Adéu!")
        break
    else:
        print("Opció no vàlida. Torna a intentar-ho.")
