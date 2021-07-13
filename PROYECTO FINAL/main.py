import pandas as pd
import listas
from tabulate import tabulate

cabeceros = ["ID", "Nombre", "Precio S/."]

compopd = tabulate(pd.DataFrame({"Componentes": listas.componentes}), headers=["Componentes"], tablefmt="fancy_grid")


def pandix(idd, name, precios):
    return tabulate(pd.DataFrame({"ID": idd,
                                  "Nombre": name,
                                  "Precios": precios}), headers=cabeceros, tablefmt='fancy_grid')


camarapd = pandix(listas.camwebid, listas.camweb, listas.camwebprecios)

casepd = pandix(listas.caseid, listas.case, listas.caseprecios)

ssdpd = pandix(listas.ssdid, listas.ssd, listas.ssdprecios)

hddpd = pandix(listas.hddid, listas.hdd, listas.hddprecios)

fuentepd = pandix(listas.fuenteid, listas.fuente, listas.fuenteprecios)

rampd = pandix(listas.ramid, listas.ram, listas.ramprecios)

monitorespd = pandix(listas.monitoresid, listas.monitores, listas.monitoresprecio)

mousepd = pandix(listas.mouseid, listas.mouse, listas.mouseprecios)

placapd = pandix(listas.placaid, listas.placa, listas.placaprecios)

intelpd = pandix(listas.intelid, listas.intel, listas.intelprecios)

amdpd = pandix(listas.amdid, listas.amd, listas.amdprecios)

tarjvideopd = pandix(listas.tarjvideoid, listas.tarjvideo, listas.tarjvideoprecios)

tecladopd = pandix(listas.tecladoid, listas.teclado, listas.tecladoprecios)

# Funcion para mostrar inventario con cantidad

cantitot = [len(listas.camwebcanti), len(listas.casecanti), len(listas.hddcanti) + len(listas.ssdcanti),
            len(listas.fuentecanti), len(listas.ramcanti), len(listas.monitorescanti),
            len(listas.mousecanti), len(listas.placacanti), len(listas.intelcanti) + len(listas.amdcanti),
            len(listas.tarjvideocanti), len(listas.tecladocanti)]

cabeceros2 = ["Nombre", "Cantidad"]


def pandixcan(name, cantidad):
    return tabulate(pd.DataFrame({"Nombre": name,
                                  "Cantidad": cantidad}), headers=cabeceros2, tablefmt='fancy_grid')


cantitotpd = pandixcan(listas.componentes, cantitot)

# Funcion para mostrar producto con cantidad

cabeceros3 = ["ID", "Nombre", "Precio S/.", "Cantidad"]

camaracantip = [listas.camwebcanti.count("001"),
                listas.camwebcanti.count("002"),
                listas.camwebcanti.count("003"),
                listas.camwebcanti.count("004"),
                listas.camwebcanti.count("005")]

casecantip = [listas.casecanti.count("006"),
              listas.casecanti.count("007"),
              listas.casecanti.count("008"),
              listas.casecanti.count("009"),
              listas.casecanti.count("010")]

ssdcantip = [listas.ssdcanti.count("011"),
             listas.ssdcanti.count("012")]

hddcantip = [listas.hddcanti.count("013"),
             listas.hddcanti.count("014"),
             listas.hddcanti.count("015")]

fuentecantip = [listas.fuentecanti.count("016"),
                listas.fuentecanti.count("017"),
                listas.fuentecanti.count("018"),
                listas.fuentecanti.count("019"),
                listas.fuentecanti.count("020")]

ramcantip = [listas.ramcanti.count("021"),
             listas.ramcanti.count("022"),
             listas.ramcanti.count("023"),
             listas.ramcanti.count("024"),
             listas.ramcanti.count("025")]

monitorescantip = [listas.monitorescanti.count("026"),
              listas.monitorescanti.count("027"),
              listas.monitorescanti.count("028"),
              listas.monitorescanti.count("029"),
              listas.monitorescanti.count("030")]

mousecantip = [listas.mousecanti.count("031"),
               listas.mousecanti.count("032"),
               listas.mousecanti.count("033"),
               listas.mousecanti.count("034"),
               listas.mousecanti.count("035")]

placacantip = [listas.placacanti.count("036"),
               listas.placacanti.count("037"),
               listas.placacanti.count("038"),
               listas.placacanti.count("039"),
               listas.placacanti.count("040")]

intelcantip = [listas.intelcanti.count("041"),
               listas.intelcanti.count("042"),
               listas.intelcanti.count("043"),
               listas.intelcanti.count("044"),
               listas.intelcanti.count("045"),
               listas.intelcanti.count("046"),
               listas.intelcanti.count("047"),
               listas.intelcanti.count("048"),
               listas.intelcanti.count("049"),
               listas.intelcanti.count("050"),
               listas.intelcanti.count("051"),
               listas.intelcanti.count("052")]

amdcantip = [listas.amdcanti.count("053"),
             listas.amdcanti.count("054"),
             listas.amdcanti.count("055"),
             listas.amdcanti.count("056")]

tarjvideocantip = [listas.tarjvideocanti.count("057"),
                   listas.tarjvideocanti.count("058"),
                   listas.tarjvideocanti.count("059"),
                   listas.tarjvideocanti.count("060"),
                   listas.tarjvideocanti.count("061")]

tecladocantip = [listas.tecladocanti.count("062"),
                 listas.tecladocanti.count("063"),
                 listas.tecladocanti.count("064"),
                 listas.tecladocanti.count("065"),
                 listas.tecladocanti.count("066")]


def pandixcan2(idd, name, precios, cantidad):
    return tabulate(pd.DataFrame({"ID": idd,
                                  "Nombre": name,
                                  "Precios": precios, "Cantidad": cantidad}), headers=cabeceros3, tablefmt='fancy_grid')


camaracantipd = pandixcan2(listas.camwebid, listas.camweb, listas.camwebprecios, camaracantip)

casecantipd = pandixcan2(listas.caseid, listas.case, listas.caseprecios, casecantip)

ssdcantipd = pandixcan2(listas.ssdid, listas.ssd, listas.ssdprecios, ssdcantip)

hddcantipd = pandixcan2(listas.hddid, listas.hdd, listas.hddprecios, hddcantip)

fuentecantipd = pandixcan2(listas.fuenteid, listas.fuente, listas.fuenteprecios, fuentecantip)

ramcantipd = pandixcan2(listas.ramid, listas.ram, listas.ramprecios, ramcantip)

monitorescantipd = pandixcan2(listas.monitoresid, listas.monitores, listas.monitoresprecio, monitorescantip)

mousecantipd = pandixcan2(listas.mouseid, listas.mouse, listas.mouseprecios, mousecantip)

placacantipd = pandixcan2(listas.placaid, listas.placa, listas.placaprecios, placacantip)

intelcantipd = pandixcan2(listas.intelid, listas.intel, listas.intelprecios, intelcantip)

amdcantipd = pandixcan2(listas.amdid, listas.amd, listas.amdprecios, amdcantip)

tarjvideocantipd = pandixcan2(listas.tarjvideoid, listas.tarjvideo, listas.tarjvideoprecios, tarjvideocantip)

tecladocantipd = pandixcan2(listas.tecladoid, listas.teclado, listas.tecladoprecios, tecladocantip)
