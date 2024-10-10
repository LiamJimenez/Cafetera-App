from cafetera import Cafetera

def main():
    cafetera = Cafetera()

    while True:
        print("\nBienvenido a la Cafetera!")
        print("1. Servir café en vaso pequeño")
        print("2. Servir café en vaso mediano")
        print("3. Servir café en vaso grande")
        print("4. Reiniciar cafetera")
        print("5. Ver cantidad de café")
        print("6. Ver cantidad de vasos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print(cafetera.servir_cafe("pequeño", 5))
        elif opcion == "2":
            print(cafetera.servir_cafe("mediano", 7))
        elif opcion == "3":
            print(cafetera.servir_cafe("grande", 10))
        elif opcion == "4":
            cafetera.reiniciar_cafetera()
            print("Cafetera reiniciada.")
        elif opcion == "5":
            print(f"Cantidad de café: {cafetera.cafe}")
        elif opcion == "6":
            print(f"Vasos pequeños: {cafetera.vasos_pequenos}")
            print(f"Vasos medianos: {cafetera.vasos_medianos}")
            print(f"Vasos grandes: {cafetera.vasos_grandes}")
        elif opcion == "0":
            print("Gracias por usar la Cafetera. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
