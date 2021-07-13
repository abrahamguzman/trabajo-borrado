import listas
import main
import pandas as pd
from tabulate import tabulate

listcotiid = []
listcotinombre = []
listcotiprecio = []

print(listcotiid)

cabeceros = ["ID", "Nombre", "Precios"]


def pandix(idd, name, precios):
    return tabulate(pd.DataFrame({"ID": idd,
                                  "Nombre": name,
                                  "Precios": precios}), headers=cabeceros, tablefmt='fancy_grid')


def mostrar(lis):
    a = 0
    for i in lis:
        a += 1
        print(str(a) + ". " + i)


def coman(x):
    com = input("\nUsted desea:\n"
                "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                "2. Ver la lista de cotización y regresar a elegir\n"
                "3. Imprimir lista de cotizaciòn con precio final y salir\n"
                )
    if com == "1":
        listas.listcoti.append(x)
        print("\nSu elemento ha sido añadido satisfactoriamente a su lista")
    elif com == "2":
        print("\nLISTA DE COTIZACIÒN:\n")
        for i in listas.listcoti:
            print(i)
    elif com == "3":
        print("")
        for i in listas.listcoti:
            print(i)


# Mostrar inventario


def mostrarinventario():
    print(main.compopd)
    opc02 = input("¿Qué producto desea ver?\n")
    if opc02 == "0":
        print(main.camarapd)
    elif opc02 == "1":
        print(main.casepd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco busca?\n"
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
        opcdisc = input("\n¿Qué marca de procesador busca?\n"
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


# Mostrar inventario con la cantidad de productos


def mostrar_inventario_cantidad():
    print(main.cantitotpd)
    opc02 = input("¿Qué producto desea ver especificamente?\n")
    if opc02 == "0":
        print(main.camaracantipd)
    elif opc02 == "1":
        print(main.casecantipd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco?\n"
                        "1. SSD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print(main.ssdcantipd)
        elif opcdisc == "2":
            print(main.hddcantipd)
    elif opc02 == "3":
        print(main.fuentecantipd)
    elif opc02 == "4":
        print(main.ramcantipd)
    elif opc02 == "5":
        print(main.monitorescantipd)
    elif opc02 == "6":
        print(main.mousecantipd)
    elif opc02 == "7":
        print(main.placacantipd)
    elif opc02 == "8":
        opcdisc = input("\n¿Marca del procesador?\n"
                        "1. Intel\n"
                        "2. AMD\n")
        if opcdisc == "1":
            print(main.intelcantipd)
        elif opcdisc == "2":
            print(main.amdcantipd)
    elif opc02 == "9":
        print(main.tarjvideocantipd)
    elif opc02 == "10":
        print(main.tecladocantipd)


def eliminar_producto():
    print(main.cantitotpd)
    opc02 = input("¿Qué producto desea eliminar?\n")
    if opc02 == "0":
        print(main.camaracantipd)
        elim = input("\nEscriba la id del producto que desee eliminar: ")
        numelim = int(input("Escriba cuántos productos desea eliminar: "))
        listas.camwebcanti.remove(elim)
        print("")
        print(numelim)
        print(main.camaracantipd)
    elif opc02 == "1":
        print(main.casecantipd)
    elif opc02 == "2":
        opcdisc = input("\n¿Wué tipo de disco?\n"
                        "1. SSD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print(main.ssdcantipd)
        elif opcdisc == "2":
            print(main.hddcantipd)
    elif opc02 == "3":
        print(main.fuentecantipd)
    elif opc02 == "4":
        print(main.ramcantipd)
    elif opc02 == "5":
        print(main.monitorescantipd)
    elif opc02 == "6":
        print(main.mousecantipd)
    elif opc02 == "7":
        print(main.placacantipd)
    elif opc02 == "8":
        opcdisc = input("\n¿Marca del procesador?\n"
                        "1. Intel\n"
                        "2. AMD\n")
        if opcdisc == "1":
            print(main.intelcantipd)
        elif opcdisc == "2":
            print(main.amdcantipd)
    elif opc02 == "9":
        print(main.tarjvideocantipd)
    elif opc02 == "10":
        print(main.tecladocantipd)


# Agregar a lista de cotización


def agregar_cot():
    print("\nElija el componente que quiere que tenga su PC:\n")
    print(main.compopd)
    opc02 = input()
    if opc02 == "0":
        print("\nTenemos estas cámaras web disponibles, por favor, elija una, escribiendo su id:")
        print(main.camarapd)
        elegir = input("\n")
        print("\nEl elemento elegido es: ", listas.camweb[listas.camwebid.index(elegir)])
        opc04 = input("\nUsted desea:\n"
                      "1. Agregar elemento a la lista de cotizacióm y regresar a elegir\n"
                      "2. Ver la lista de cotización y regresar a elegir\n")
        if opc04 == "1":
            listcotiid.append(elegir)
            listcotinombre.append(listas.camweb[listas.camwebid.index(elegir)])
            listcotiprecio.append(listas.camwebprecios[listas.camwebid.index(elegir)])
            print("El elemento fue añadido a la lista exitosamente.\n")
        elif opc04 == "2":
            listcotiid.append("---")
            listcotinombre.append("PRECIO TOTAL")
            preciofinal = 0
            for i in listcotiprecio:
                preciofinal += float(i)
            listcotiprecio.append(str(preciofinal))
            print(pandix(listcotiid, listcotinombre, listcotiprecio))

    elif opc02 == "1":
        print("\nTenemos estos case disponibles, por favor elija uno:")
        mostrar(listas.case)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.case[elegir])
        coman(listas.case[elegir])
    elif opc02 == "2":
        opcdisc = input("\nElija un tipo de disco duro:\n"
                        "1. SDD\n"
                        "2. HDD\n")
        if opcdisc == "1":
            print("\nEstos son los discos SSD disponibles, por favor elija uno:")
            mostrar(listas.ssd)
            elegir = int(input()) - 1
            print("\nEl elemento elegido es: ", listas.ssd[elegir])
            coman(listas.ssd[elegir])
        elif opcdisc == "2":
            print("\nEstos son los discos HDD disponibles, por favor elija uno:")
            mostrar(listas.hdd)
            elegir = int(input()) - 1
            print("\nEl elemento elegido es: ", listas.hdd[elegir])
            coman(listas.hdd[elegir])
    elif opc02 == "3":
        print("\nTenemos estas fuentes de poder disponibles, por favor elija una:")
        mostrar(listas.fuente)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.fuente[elegir])
        coman(listas.fuente[elegir])
    elif opc02 == "4":
        print("\nTenemos estas memorias RAM disponibles, por favor elija una:")
        mostrar(listas.ram)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.ram[elegir])
        coman(listas.ram[elegir])
    elif opc02 == "5":
        print("\nTenemos estos monitores disponibles, por favor elija uno:")
        mostrar(listas.monitores)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.monitores[elegir])
        coman(listas.monitores[elegir])
    elif opc02 == "6":
        print("\nTenemos estos mouses disponibles, por favor elija uno:")
        mostrar(listas.mouse)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.mouse[elegir])
        coman(listas.mouse[elegir])
    elif opc02 == "7":
        print("\nTenemos estas placas madre disponibles, por favor elija una:")
        mostrar(listas.placa)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.placa[elegir])
        coman(listas.placa[elegir])
    elif opc02 == "8":
        opcproce = input("\nPor favor elija una marca de procesador:\n"
                         "1. Intel\n"
                         "2. AMD\n")
        if opcproce == "1":
            print("Estos son los procesadores Intel disponibles, por favor elija uno")
            mostrar(listas.intel)
            elegir = int(input()) - 1
            print("\nEl elemento elegido es: ", listas.intel[elegir])
            coman(listas.intel[elegir])
        elif opcproce == "2":
            print("Estos son los procesadores AMD disponibles, por favor elija uno")
            mostrar(listas.amd)
            elegir = int(input()) - 1
            print("\nEl elemento elegido es: ", listas.amd[elegir])
            coman(listas.amd[elegir])
    elif opc02 == "9":
        print("\nTenemos estas tarjetas de video disponibles, por favor elija una:")
        mostrar(listas.tarjvideo)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.tarjvideo[elegir])
        coman(listas.tarjvideo[elegir])
    elif opc02 == "10":
        print("\nTenemos estos teclados disponibles, por favor elija uno:")
        mostrar(listas.teclado)
        elegir = int(input()) - 1
        print("\nEl elemento elegido es: ", listas.teclado[elegir])
        coman(listas.teclado[elegir])


elegire = "001"


def agregarcot(nom):
    listcotiid.append(elegire)
    listcotinombre.append("listas." + nom["listas." + nom + "id".index(elegire)])
    listcotiprecio.append("listas." + nom + "precios"["listas." + nom + "id".index(elegire)])


print(listcotiid)
print(listcotinombre)
print(listcotiprecio)
