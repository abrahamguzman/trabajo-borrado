import funciones

import main

while True:
    rol = input("Bienvenido a PC'S GOSU, donde usted tiene el derecho de tener lo mejor. \n"
                "\n"
                "Soy:\n"
                "\n"
                "1. Admin\n"
                "2. Cliente\n"
                "3. Salir\n")

    # Salir

    if rol == "3":
        break

    # Admin

    elif rol == "1":
        while True:
            print("")
            print("*" * 130)
            print("")
            n = (input("1. Iniciar Sesión\n"
                       "2. Ver Inventario\n"
                       "3. Eliminar productos\n"
                       "4. Agregar productos\n"
                       "5. Informe de ventas\n"
                       "6. Salir\n"))
            if n == "6":
                break
            elif n == "2":
                funciones.mostrar_inventario_cantidad()
            elif n == "3":
                funciones.eliminar_producto()
    elif rol == "2":
        while True:
            print("")
            print("*" * 130)
            print("")
            opc01 = input("Buenas, ¿En qué podemos ayudarle?:\n\n"
                          "1. Ver productos\n"
                          "2. Ver promociones\n"
                          "3. Hacer cotizaciones\n"
                          "4. Ver locales y horarios de atención\n"
                          "5. Retroceder\n")
            # Retroceder
            if opc01 == "5":
                break
            # Ver Productos
            elif opc01 == "1":
                print(main.compopd)
                opc02 = input("¿Qué producto desea ver?\n")
                if opc02 == "0":
                    print(main.camarapd)
                elif opc02 == "1":
                    print(main.casepd)
                elif opc02 == "2":
                    opcdisc = input("\n¿En qué tipo de disco está interesado?\n"
                                    "1. SSD\n"
                                    "2. HDD\n")
                    if opcdisc == "1":
                        print(main.ssdpd)
                    elif opcdisc == "2":
                        print(main.hddpd)
                elif opc02 == "3":
                    print(main.fuentepd)
                elif opc02 == "4":
                    print(main.rampd)
                elif opc02 == "5":
                    print(main.monitorespd)
                elif opc02 == "6":
                    print(main.mousepd)
                elif opc02 == "7":
                    print(main.placapd)
                elif opc02 == "8":
                    opcdisc = input("\n¿En qué marca de procesador está interesado??\n"
                                    "1. Intel\n"
                                    "2. AMD\n")
                    if opcdisc == "1":
                        print(main.intelpd)
                    elif opcdisc == "2":
                        print(main.amdpd)
                elif opc02 == "9":
                    print(main.tarjvideopd)
                elif opc02 == "10":
                    print(main.tecladopd)

            # Lista de cotizaciones

            elif opc01 == "3":
                while True:
                    funciones.agregar_cot()
            elif opc01 == "4":
                break
