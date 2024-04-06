from classes.lista_piatti import ListaPiatti
import interfaces.interfaccia_testuale as cli
import interfaces.interfaccia_grafica as gui

MODE = "CLI"

try:

    if MODE == "CLI":
        nomefile = "./files/lista piatti.xlsx"
        #nomefile = input("Percorso file excel: ")

        #lettura dei dati da file excel
        lista_piatti = ListaPiatti()
        lista_piatti.read(nomefile)

        function_number = -1
        while function_number != "0":
            #menù scelte
            function_number = cli.menu()

            #switch per il menù scelte
            match function_number:
                case "0":
                    pass
                case "1":
                    port = cli.chiedi_portata()
                    base = cli.chiedi_base()
                    piatto = lista_piatti.piatto_a_caso(port,base)
                    cli.print_risultato_ricerca(piatto)
                case "2":
                    port = cli.chiedi_portata()
                    base = cli.chiedi_base()
                    ingr = cli.chiedi_ingredienti()
                    piatto = lista_piatti.piatto_a_caso(port,base,ingr)
                    cli.print_risultato_ricerca(piatto)
                case "3":
                    port = cli.chiedi_portata()
                    base = cli.chiedi_base()
                    lista_temp = lista_piatti.tutti_i_piatti(port,base)
                    cli.print_risultato_ricerca(lista_temp)
                case "4":
                    port = cli.chiedi_portata()
                    base = cli.chiedi_base()
                    ingr = cli.chiedi_ingredienti()
                    lista_temp = lista_piatti.tutti_i_piatti(port,base,ingr)
                    cli.print_risultato_ricerca(lista_temp)
                case _:
                    print("Funzione non presente")

    elif MODE == "GUI":
        gui.start_gui()

except Exception as e:
    print("Try except esterno")
    print(e)
    input("Premi invio per uscire...")