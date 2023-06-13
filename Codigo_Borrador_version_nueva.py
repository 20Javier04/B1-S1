# ____________________________________________________________________
#/                                                                    \
#|              Energía y trabajo de la fuerza de roce                |
#|                     (Sistema no conservativo)                      |
#|                                                                    |
#| by: Javier Muñoz, Abdiel Molina, Tomas Ahumada, Yadhira Zambrano   |
#\____________________________________________________________________/
#----------------------------------------------------------------------
# Librerias
#----------------------------------------------------------------------
import pygame as PG, tkinter as TK, sys, os
from tkinter import ttk ; from pygame.locals import *
#----------------------------------------------------------------------
# Constantes
#----------------------------------------------------------------------
nRES = (600, 400) ; lOk = True ; G = 10 ; LM1 = 180; COS180 = -1 ; 
px = 26 ; py = 107

# ____________________________________________________________________
#/                                                                    \
#|        /Parte del codigo relacionada con la ventana Pygame\        |
#\____________________________________________________________________/
#----------------------------------------------------------------------
# Crear Pantalla Pygame
#----------------------------------------------------------------------
def PVentana(nRES):
    PG.init()
    ventana = PG.display.set_mode(nRES)
    nVentana  = PG.display.set_caption('simulacion')
    fuente = PG.font.SysFont("Arial", 18)
    return ventana
#----------------------------------------------------------------------
# cargar imagenes en formato Pygame
#----------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except (PG.error) as message:
            raise SystemExit (message)
    image = image.convert()
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color,RLEACCEL)
    return image
#----------------------------------------------------------------------
# cargar imagenes en formato Pygame
#----------------------------------------------------------------------
def Fig_Init():
    aImg = []
    aImg.append(Load_Image('fondo.png',False )) # fondo    |0
    aImg.append(Load_Image('pelota.png',True )) # pelota   |1
    aImg.append(Load_Image('base.png',True ))   # base     |2
    return aImg
#-----------------------------------------------------------------------
# Pintar el fondo de la ventana pygame
#-----------------------------------------------------------------------
def Pinta_Pantalla():
    Pantalla.blit(aSprt[0],(0,0))
    return
#-----------------------------------------------------------------------
# Pintar la pelota en la ventana pygame
#-----------------------------------------------------------------------
def Pinta_Pelota():
    Pantalla.blit(aSprt[1],(px,py))
    return
#-----------------------------------------------------------------------
# Pintar la base en la ventana pygame
#-----------------------------------------------------------------------
def Pinta_base():
    Pantalla.blit(aSprt[2],(19,128))
    return
#-----------------------------------------------------------------------
# simulacion del caso 1
#-----------------------------------------------------------------------
def Mover_Pelota():
    global px, py
    if px < 148:
        px += 1.2 * 1.5
        py += 2 * 1.5
    elif px < 357:
        px += 2.5
    elif px < 520 or py > 183:
        px += 2
        py -= 1.43

#-----------------------------------------------------------------------
# actualizacion de pygame
#-----------------------------------------------------------------------
def Actualizar_Pantalla():
    frame.update()
    Mover_Pelota()
    Pinta_Pantalla()
    Pinta_base()
    Pinta_Pelota()
    PG.display.flip()
# ----------------------------------------------------------------------
# bucle while del codigo pygame
# ----------------------------------------------------------------------
def Iniciar_Simulacion():
    global lOk
    lOk = True
    px = 26
    py = 107 
    while lOk:
        for event in PG.event.get():
            if event.type == PG.QUIT:
                lOk = False
            if event.type == PG.KEYDOWN:
                if event.key == PG.K_ESCAPE:
                    lOk = False

        cKey = PG.key.get_pressed()
        if cKey[PG.K_ESCAPE]:
            lOk = False

        Actualizar_Pantalla()
        clock.tick(60)

    PG.quit()
    sys.exit()

# ____________________________________________________________________
#/                                                                    \
#|       /Parte del codigo relacionada con la ventana Tkinter\        |
#\____________________________________________________________________/

#----------------------------------------------------------------------
# Crear Pantalla Tkinter
#----------------------------------------------------------------------
window = TK.Tk() ; window.title("Datos") ; window.geometry("800x700")
#----------------------------------------------------------------------
# caso 1
#----------------------------------------------------------------------
def caso1(m, h1, h2, dx, G, COS180):
   Emeca = m * G * h1
   Emecd = m * G * h2
   Wfnc = Emecd - Emeca
   Fr = Wfnc / (dx * COS180)

   result_text = f'''Eme ca: {Emeca} J\nEme cd: {Emecd} J\nWfnc: {Wfnc} J\nFr: {Fr} N'''
   result_label.config(text=result_text)

def calculate_energy():
    m = float(masa_entry.get())
    h1 = float(altura_a_entry.get())
    h2 = float(altura_d_entry.get())
    dx = float(distancia_roce_entry.get())
    caso1(m, h1, h2, dx, G, COS180)
#----------------------------------------------------------------------
# cracion de botones
#----------------------------------------------------------------------
masa_label = TK.Label(window, text="Masa:")
masa_label.pack()
masa_entry = TK.Entry(window)
masa_entry.pack()

altura_a_label = TK.Label(window, text="Altura A:")
altura_a_label.pack()
altura_a_entry = TK.Entry(window)
altura_a_entry.pack()

altura_d_label = TK.Label(window, text="Altura D:")
altura_d_label.pack()
altura_d_entry = TK.Entry(window)
altura_d_entry.pack()

distancia_roce_label = TK.Label(window, text="Distancia de roce:")
distancia_roce_label.pack()
distancia_roce_entry = TK.Entry(window)
distancia_roce_entry.pack()

calculate_button = TK.Button(window, text="Calcular", command=calculate_energy)
calculate_button.pack()

start_simulation_button = TK.Button(window, text="Iniciar Simulacion", command=Iniciar_Simulacion)
start_simulation_button.pack()

result_label = TK.Label(window, text="")
result_label.pack()

# ____________________________________________________________________
#/                                                                    \
#|                     /unificacion de ventanas\                      |
#\____________________________________________________________________/
#----------------------------------------------------------------------
# Juntar las 2 ventanas
#----------------------------------------------------------------------
frame = TK.Frame(window, width=600, height=400)
frame.pack()

os.environ["SDL_WINDOWID"] = str(frame.winfo_id()) 
os.environ["SDL_VIDEODRIVER"] = "windib" 

screen = PVentana(nRES)
# ____________________________________________________________________
#/                                                                    \
#|             /bucle en el cual se ejecuta el programa\              |
#\____________________________________________________________________/
#----------------------------------------------------------------------
Pantalla = PVentana(nRES)
aSprt = Fig_Init()
clock = PG.time.Clock()
#----------------------------------------------------------------------
window.mainloop()

