from tkinter import *
import tkinter.ttk as ttk
import os
from tkinter import messagebox
import time

SIN_CATEGORIA = "-1"
JUEGOS = "0"
MUSICA = "1"
LIBROS = "2"
REDES_SOCIALES = "3"
UTILIDADES = "4"

#coordenadas de los botones
COORDS_BOTONES=[[5,5],[210,5],[440,5],[670,5],[880, 5],[5,200],[200,200],[400,200]]
#categorias del combobox
CATEGORIAS = ["-Sin categoria-", "Juegos", "Libros", "Musica", "Redes sociales", "Utilidades" ]
BOTONES = []

window = Tk()
window.minsize(1300, 700)
window.maxsize(1300, 700)
window.geometry("1300x700+25+0")
window.title("Modo Compra")
window.config(bg="#001939")

def AbrirArchivo(archivo, modo): #abre el archivo
    file = open(archivo, modo)
    return file

def unirLista(matriz):
    if matriz == []:
        return []
    else:
        return [";".join(matriz[0])] + unirLista(matriz[1:])
    
def separarApps(i): 
    if i == len(listaApps):
        return
    listaApps[i] = listaApps[i].replace("\n", "").split(";")
    separarApps(i + 1)
    
def separarUsuarios(i): 
    if i == len(listaUsuarios):
        return
    listaUsuarios[i] = listaUsuarios[i].replace("\n", "").split(";")
    separarUsuarios(i + 1)

archivo = AbrirArchivo("Apps.txt", "r")
listaApps = archivo.readlines() #lo convierte en una lista
separarApps(0) #llama la funcion separarListas
archivo.close

archivo2 = AbrirArchivo("Usuarios.txt", "r")
listaUsuarios = archivo2.readlines() #lo convierte en una lista
separarUsuarios(0) #llama la funcion separarListas
archivo2.close

POS_USUARIO = 0
POS_CONTRASEÑA = 1
POS_CONTRASEÑA2 = 2
POS_PAIS = 3

POS_ID_VENDEDOR = 0
POS_ID_PRODUCTO = 1
POS_CATEGORIA = 2
POS_DESCRIPCION = 3
POS_PRECIO = 4
POS_ESTADO = 5
POS_SCREENSHOT1 = 6
POS_SCREENSHOT2 = 7
POS_DOWNLOADS = 8
POS_DOWNLOADSCR = 9

def cargar_imagen(nombre): #Cargar imagenes
    ruta = os.path.join("imagenes", nombre)
    imagen = PhotoImage(file = ruta)
    return imagen

carrito = cargar_imagen("carrito.gif")
Mario1  = cargar_imagen(listaApps[0][POS_SCREENSHOT1])
Mario2 = cargar_imagen(listaApps[0][POS_SCREENSHOT2])
Pokemon1  = cargar_imagen(listaApps[1][POS_SCREENSHOT1])
Pokemon2 = cargar_imagen(listaApps[1][POS_SCREENSHOT1])
Candy1  = cargar_imagen(listaApps[2][POS_SCREENSHOT1])
Candy2 = cargar_imagen(listaApps[2][POS_SCREENSHOT1])
Wattpad1  = cargar_imagen(listaApps[3][POS_SCREENSHOT1])
Wattpad2 = cargar_imagen(listaApps[3][POS_SCREENSHOT1])
Telegram1  = cargar_imagen(listaApps[4][POS_SCREENSHOT1])
Telegram2 = cargar_imagen(listaApps[4][POS_SCREENSHOT1])
GoogleMaps1  = cargar_imagen(listaApps[5][POS_SCREENSHOT1])
GoogleMaps2 = cargar_imagen(listaApps[5][POS_SCREENSHOT1])
Youtube1  = cargar_imagen(listaApps[6][POS_SCREENSHOT1])
Youtube2 = cargar_imagen(listaApps[6][POS_SCREENSHOT1])
Kindle1  = cargar_imagen(listaApps[7][POS_SCREENSHOT1])
Kindle2 = cargar_imagen(listaApps[7][POS_SCREENSHOT1])


label_carrito = Label(window, image = carrito)
label_carrito.place (x = 600, y = 5)

labelPrincipal = Canvas(window, width = 1200, height = 500, bg = "#001939", highlightthickness = 0)
labelPrincipal.place(x=-1, y = 100)


def buscar(event):
    busqueda = entradaDeTexto.get()
    # Toma la categoria que se ingreso en el Combo Box
    categoria = comboboxCategorias.get()
    if busqueda == "" and categoria.lower() == "-sin categoria-": #si el usuario no escogió nada, 
        buscarAux("", "", 0) #me muestra todas las apps
    # Se verifica si la categoria es juegos
    elif categoria.lower() == "juegos": #si la categoria es juegos
        # Enviar a la funcion la categoria y el indice desde donde empieza
        buscarAux(busqueda.lower(), JUEGOS, 0)
    elif categoria.lower() == "musica":#si la categoria es música
        buscarAux(busqueda.lower(), MUSICA, 0)
    elif categoria.lower() == "libros":#si la categoria es libros
        buscarAux(busqueda.lower(), LIBROS, 0)
    elif categoria.lower() == "redes sociales":#si la categoria es redes sociales
        buscarAux(busqueda.lower(), REDES_SOCIALES, 0)
    elif categoria.lower() == "utilidades":#si la categoria es tilidades
        buscarAux(busqueda.lower(), UTILIDADES, 0)
    else:
        messagebox.showerror("Error", "No existe esa categoría")



def buscarAux(entrada, categoria, cont):#i es un contador, categoria es la categoria de la aplicacion (0, 1, 2, 3...), entrada es lo que el usuario ingreso en el entry
    if cont == len(listaApps):
        return None
    elif entrada == "" and categoria == "": #entrada y categoria vacios
        BOTONES[cont].place(x=COORDS_BOTONES[cont][0],y=COORDS_BOTONES[cont][1])
    elif entrada != "" and categoria == "": #si el usuario escribe algo en el entry, y categoria es vacia
        if entrada in listaApps[cont][POS_ID_PRODUCTO].lower(): #si lo que el usuario escribio en el entry esta en la descripcion (pos[3])

            BOTONES[cont].place(x=COORDS_BOTONES[cont][0],y=COORDS_BOTONES[cont][1])
        else:
            BOTONES[cont].place_forget()
    elif entrada == "" and categoria != "": #si nombre es vacio, y categorias tiene algo
        if listaApps[cont][POS_CATEGORIA] == categoria: #verifica que la categoria(JUEGOS, MUSICA...), este en la posicion de categorias del archivo

            BOTONES[cont].place(x=COORDS_BOTONES[cont][0],y=COORDS_BOTONES[cont][1])
        else:
            BOTONES[cont].place_forget()

    elif entrada != "" and categoria != "":
        if listaApps[cont][POS_CATEGORIA] == categoria and entrada in listaApps[cont][POS_ID_PRODUCTO].lower(): #si se escogio categoria Y se escribio algo en el entry

            BOTONES[cont].place(x=COORDS_BOTONES[cont][0],y=COORDS_BOTONES[cont][1])
        else:
            BOTONES[cont].place_forget()
    buscarAux(entrada, categoria, cont + 1) #i aumenta para recorrer toda la lista

#entradaPais como global para que lo lea en varias ventanas
entradaPais = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")

def crear_vent ( ):
    window.withdraw ( ) #"oculta" la ventana principal 
    vent = Toplevel ( ) # es para crear una ventana secudaria
    vent.title("Ingresar")
    vent.minsize (450, 400)
    labelPrincipal = Canvas (vent, width = 450, height = 400, bg = "#001939")
    labelPrincipal.place (x = -1, y = -1)
    def volver( ):
        vent.destroy ( )
        window.deiconify( )
    boton = Button (vent, text = "Volver", font = ("Helvetica", 12), width = 6, command = volver)
    boton.place (x = 300, y = 360)

    labelSR = Label(labelPrincipal, text = "SISTEMA DE REGISTRO", bg = "white", fg = "black", font = ("arial", 12))
    labelSR.place (x = 5, y = 20)
    labelNombre = Label(labelPrincipal, text = "Nombre de usuario:", font = ("arial bold", 12), bg = "#001939", fg = "white")
    labelNombre.place (x = 140, y = 50)
    entradaNombre = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")
    entradaNombre.place (x = 105, y = 80)
    labelContra = Label(labelPrincipal, text = "Contraseña:", font = ("arial bold", 12) ,bg = "#001939", fg = "white")
    labelContra.place (x = 165, y = 110)
    entradaContra = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")
    entradaContra.place (x = 105, y = 140)
    labelVerContra = Label(labelPrincipal, text = "Verificar contraseña:", font = ("arial bold", 12), bg = "#001939", fg = "white")
    labelVerContra.place (x = 140, y = 170)
    entradaVerContra = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")
    entradaVerContra.place (x = 105, y = 200)
    labelCorreo = Label(labelPrincipal, text = "Correo:", font = ("arial bold", 12), bg = "#001939", fg = "white")
    labelCorreo.place (x = 180, y = 230)
    entradaCorreo = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")
    entradaCorreo.place (x = 105, y = 260)
    labelPais = Label(labelPrincipal, text = "Pais:", font = ("arial bold", 12), bg = "#001939", fg = "white")
    labelPais.place (x = 190, y = 290)
    entradaPais = Entry (labelPrincipal, font = ("arial", 12), width = 25, bg = "white")
    entradaPais.place (x = 105, y = 330)
    
    def registrar(): #funcion para agregar usuarios
        if entradaNombre.get() != "" and entradaContra.get() != "" and entradaVerContra.get() != "" and entradaCorreo.get() != "" and entradaPais.get() != "": #si las entradas no esta vacias
            if entradaPais.get() == "Costa Rica" or entradaPais.get() == "Otro":
                if entradaContra.get() == entradaVerContra.get():
                    registrar = open("Usuarios.txt", "a") #abre un archivo
                    registrar.write( "\n" + entradaNombre.get() + ";" + entradaContra.get() + ";" + entradaVerContra.get() + ";" + entradaPais.get()) #escribe en el archivo
                    registrar.close()
                    vent.destroy()
                    window.deiconify() #al regustrarse lo devuelve a la ventana
                else:
                    messagebox.showerror("Error en los datos", "Las contraseñas no coinciden")
            else:
                messagebox.showerror("Error en los datos", "Pais debe ser Costa Rica u Otro")
        else:
            messagebox.showerror("Error en los datos", "Debe llenar todos los campos")
                            
                         
    boton2 = Button (labelPrincipal, text = "Registrarse", font = ("arial", 12), width = 10, command = registrar) #llama a a funcion de registrar
    boton2.place (x = 180, y = 360)        



boton = Button (window, text = "Sistema de registro", font = ("arial", 12), width = 20, bg = "white", fg = "#001939", command = crear_vent) #al apretar el botón, el comando que se llama es la funcion
boton.place (x = 1000, y = 65)

def ventanaApps(i): #una sola ventana para todos los botones, que me muestra la informaion de cada app
    window.withdraw ( )
    ventanaApps1 = Toplevel( )
    ventanaApps1.title("MostrarAplicacion")
    ventanaApps1.minsize(600, 600)
    ventanaApps1.resizable(width = NO, height  = NO)
    ventanaApps1.config(bg="#001939")

    def volver( ):
        ventanaApps1.destroy ( )
        window.deiconify( )
    boton = Button (ventanaApps1, text = "Volver", font = ("Helvetica", 12), width = 6, command = volver)
    boton.place (x = 500, y = 560)

    def ventanaApps2(i):
        global entradaPais, listaApps, listaUsuarios
        vent2 = Toplevel ( ) # es para crear una ventana secudaria
        vent2.title("Ingresar")
        vent2.minsize (250, 200)
        labelPrincipal = Canvas (vent2, width = 400, height = 400, bg = "#001939")
        labelPrincipal.place (x = -1, y = -1)
            
        def verificar(i):#verifica que el usuario ya esté registrado
            global listaUsuarios
            if i == len(listaUsuarios):
                messagebox.showerror("Error", "Usuario no encontrado. Debe registrarse")
            elif entryUsuario.get() != listaUsuarios[i][POS_USUARIO]:
                verificar(i + 1)
            else:
                descargarApp(i)
        lbUsuario = Label(labelPrincipal, text = "Ingrese su nombre de usuario")
        lbUsuario.place(x=80, y = 60)
        entryUsuario = Entry(labelPrincipal)
        entryUsuario.place(x = 100, y = 100)
        btnVerificar = Button(labelPrincipal, text = "Descargar", command = lambda: verificar(0))
        btnVerificar.place(x = 100, y = 150)
                
        def descargarApp(i):
            global listaUsuarios, listaApps
            if listaUsuarios[i][POS_PAIS] == "Costa Rica":
                listaApps[i][POS_DOWNLOADSCR] = str(int(listaApps[i][POS_DOWNLOADSCR]) + 1) #suma una descarga de Costa Rica cada vez que se llama la funcion
                usuarios = "\n".join(unirLista(listaUsuarios))#llama la funcion unirListas
                usuariosFile = open("Usuarios.txt", "w")
                usuariosFile.write(str(usuarios))
                aplicaciones = "\n".join(unirLista(listaApps))
                aplicacionesFile = open("Apps.txt", "w")
                aplicacionesFile.write(str(aplicaciones))
                time.sleep(2)
                btnVerificar.config(text = "Instalando")
                btnVerificar.config(text = "Descargar")
                usuariosFile.close()
                aplicacionesFile.close()
                messagebox.showinfo("Listo", "Descarga completada")
            else:
                listaApps[i][POS_DOWNLOADS] = str(int(listaApps[i][POS_DOWNLOADS]) + 1 + int(listaApps[i][POS_DOWNLOADSCR])) #suma una descarga cada vez que se llama la funcion
                usuarios = "\n".join(unirLista(listaUsuarios))
                usuariosFile = open("Usuarios.txt", "w")
                usuariosFile.write(str(usuarios))
                aplicaciones = "\n".join(unirLista(listaApps))
                aplicacionesFile = open("Apps.txt", "w")
                aplicacionesFile.write(str(aplicaciones))
                time.sleep(2)
                btnVerificar.config(text = "Instalando")
                btnVerificar.config(text = "Descargar")
                usuariosFile.close()
                aplicacionesFile.close()
    nombreApp = Label(ventanaApps1, text = listaApps[i][3], bg = "#001939", fg = "white")
    nombreApp.place(x=10, y=300)
    screenShot1 = cargar_imagen(listaApps[i][POS_SCREENSHOT1])
    labelSS1 = Label(ventanaApps1, image = screenShot1)
    labelSS1.image = screenShot1
    labelSS1.place(x=50, y=50)
    screenShot2 = cargar_imagen(listaApps[i][POS_SCREENSHOT2])
    labelSS2 = Label(ventanaApps1, image = screenShot2)
    labelSS2.image = screenShot2
    labelSS2.place(x=350, y=50)
    descargas = Label(ventanaApps1, text = listaApps[i][POS_DOWNLOADS], bg = "#001939", fg = "white")
    descargas.place(x=10, y=400)
    descargasCR = Label(ventanaApps1, text = listaApps[i][POS_DOWNLOADSCR], bg = "#001939", fg = "white")
    descargasCR.place(x=10, y=450)

    
    btnPrecio = Button(ventanaApps1, text = listaApps[i][POS_PRECIO], bg = "white", fg = "#001939", width = 7, command = lambda: ventanaApps2(i)) #boton para descargar
    btnPrecio.place(x=100, y=470)
    

Mario = Button (labelPrincipal, width = 180, height = 135, bg = "#001939", image = Mario1, command=lambda: ventanaApps(0))
Mario.place(x=COORDS_BOTONES[0][0],y=COORDS_BOTONES[0][1])
BOTONES.append(Mario)
Pokemon = Button (labelPrincipal, width = 200, height = 133, bg = "#001939", image = Pokemon1,command=lambda: ventanaApps(1))
Pokemon.place(x=COORDS_BOTONES[1][0], y=COORDS_BOTONES[1][1])
BOTONES.append(Pokemon)
Candy = Button (labelPrincipal, width = 200, height = 142, bg = "#001939", image = Candy1,command=lambda: ventanaApps(2))
Candy.place(x=COORDS_BOTONES[2][0], y=COORDS_BOTONES[2][1])
BOTONES.append(Candy)
Wattpad = Button (labelPrincipal, width = 170, height = 153, bg = "#001939", image = Wattpad1,command=lambda: ventanaApps(3))
Wattpad.place(x=COORDS_BOTONES[3][0], y=COORDS_BOTONES[3][1])
BOTONES.append(Wattpad)
Telegram = Button (labelPrincipal, width = 150, height = 150, bg = "#001939", image = Telegram1,command=lambda: ventanaApps(4))
Telegram.place(x=COORDS_BOTONES[4][0], y=COORDS_BOTONES[4][1])
BOTONES.append(Telegram)
GoogleMaps = Button (labelPrincipal, width = 150, height = 146, bg = "#001939", image = GoogleMaps1,command=lambda: ventanaApps(5))
GoogleMaps.place(x=COORDS_BOTONES[5][0], y=COORDS_BOTONES[5][1])
BOTONES.append(GoogleMaps)
Youtube = Button (labelPrincipal, width = 180, height = 135, bg = "#001939", image = Youtube1,command=lambda: ventanaApps(6))
Youtube.place(x=COORDS_BOTONES[6][0], y=COORDS_BOTONES[6][1])
BOTONES.append(Youtube)
Kindle = Button (labelPrincipal, width = 150, height = 150, bg = "#001939", image = Kindle1,command=lambda: ventanaApps(7))
Kindle.place(x=COORDS_BOTONES[7][0], y=COORDS_BOTONES[7][1])
BOTONES.append(Kindle)   




lbWelcome = Label(window, text="AStore", font=("Helvetica", 30), bg="#001939", fg="white")
lbWelcome.place(x=450, y=10)

entradaDeTexto = Entry(window, width = 40, font = ("Helvetica", 15))
entradaDeTexto.place(x=250, y=70)
entradaDeTexto.bind("<Return>", buscar)

comboboxCategorias = ttk.Combobox(window, values=CATEGORIAS, font = ("Helvetica", 15))
comboboxCategorias.set("-Sin categoria-")
comboboxCategorias.grid(row=1, column=1, columnspan=3)
comboboxCategorias.place(x=700, y=68)
comboboxCategorias.bind("<<ComboboxSelected>>", buscar)






window.mainloop()
