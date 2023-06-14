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
# Pintar los datos en la ventana pygame
#-----------------------------------------------------------------------
def Pinta_datos():
    global m, h1, h2, dx
    
    fuente = PG.font.Font(None, 24)
    tAlturaA = fuente.render(f'A: {h1}m', False, (0, 0, 0))
    tAlturaD = fuente.render(f'D: {h2}m', False, (0, 0, 255))
    tDRoce = fuente.render(f'Distancia de Roce: {dx}m', False, (128, 0, 128))
    
    Pantalla.blit(tAlturaA, (19,120))
    Pantalla.blit(tAlturaD, (530,210))
    Pantalla.blit(tDRoce, (200,340))
    return
#-----------------------------------------------------------------------
# simulacion del caso 1
#-----------------------------------------------------------------------
def Mover_Pelota():
    global px, py, h1, h2, dx, Fr, G
    if px < 148:
        px += 1.2 * (h1/G)
        py += 2 * (h1/G)
    elif px < 357:
        px += 2.5 * (dx/Fr+0.55)
    elif px < 520 or py > 183:
        px += 2 * (h2/Fr+0.5)
        py -= 1.43 * (h2/Fr+0.5)
#-----------------------------------------------------------------------
# actualizacion de pygame
#-----------------------------------------------------------------------
def Actualizar_Pantalla():
    frame.update()
    Mover_Pelota()
    Pinta_Pantalla()
    Pinta_base()
    Pinta_Pelota()
    Pinta_datos()
    PG.display.flip()
#-----------------------------------------------------------------------
# cerrar pygame
#-----------------------------------------------------------------------
def cerrar_ventana():
    PG.quit()
    window.destroy()
#-----------------------------------------------------------------------
# reiniciar pygame
#-----------------------------------------------------------------------
def reiniciar_simulacion():
    global px, py, m, h1, h2, dx

    px = 26
    py = 107
    m = 0
    h1 = 0
    h2 = 0
    dx = 0
    
    Iniciar_Simulacion()

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
            cerrar_ventana()
            
        Actualizar_Pantalla()
        clock.tick(60)

# ____________________________________________________________________
#/                                                                    \
#|       /Parte del codigo relacionada con la ventana Tkinter\        |
#\____________________________________________________________________/

#----------------------------------------------------------------------
# Crear Pantalla Tkinter
#----------------------------------------------------------------------
window = TK.Tk() ; window.title("Datos") ; window.geometry("800x700")
#----------------------------------------------------------------------
# caso 1 (Todos los datos)
#----------------------------------------------------------------------
def caso1(m, h1, h2, dx, G, COS180):
   global Fr
   Emeca = m * G * h1
   Emecd = m * G * h2
   Wfnc = Emecd - Emeca
   Fr = Wfnc / (dx * COS180)

   result_text = f'''Eme ca: {Emeca} J\nEme cd: {Emecd} J\nWfnc: {Wfnc} J\nFr: {Fr} N'''
   result_label.config(text=result_text)
#----------------------------------------------------------------------
def calculate_energy():
    global m, h1, h2, dx
    m = float(masa_entry.get())
    h1 = float(altura_a_entry.get())
    h2 = float(altura_d_entry.get())
    dx = float(distancia_roce_entry.get())
    caso1(m, h1, h2, dx, G, COS180)
    return m, h1, h2, dx
#----------------------------------------------------------------------
# Almacenamiento de datos
#----------------------------------------------------------------------
m = 0 ; h1 = 0 ; h2 = 0 ; dx = 0 ; Fr = 0
#----------------------------------------------------------------------
# creacion de botones
#----------------------------------------------------------------------
masa_label = TK.Label(window, text="Masa(kg)")
masa_label.pack()
masa_entry = TK.Entry(window)
masa_entry.pack()
#----------------------------------------------------------------------
altura_a_label = TK.Label(window, text="Altura A(m)")
altura_a_label.pack()
altura_a_entry = TK.Entry(window)
altura_a_entry.pack()
#----------------------------------------------------------------------
altura_d_label = TK.Label(window, text="Altura D(m)")
altura_d_label.pack()
altura_d_entry = TK.Entry(window)
altura_d_entry.pack()
#----------------------------------------------------------------------
distancia_roce_label = TK.Label(window, text="Distancia de roce(m)")
distancia_roce_label.pack()
distancia_roce_entry = TK.Entry(window)
distancia_roce_entry.pack()
#----------------------------------------------------------------------
calculate_button = TK.Button(window, text="Calcular", command=calculate_energy)
calculate_button.pack()
#----------------------------------------------------------------------
result_label = TK.Label(window, text="")
result_label.pack()
#----------------------------------------------------------------------
reiniciar_simulacion_button = TK.Button(window, text="Iniciar Simulacion", command=reiniciar_simulacion)
reiniciar_simulacion_button.pack()

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
window.protocol("WM_DELETE_WINDOW", cerrar_ventana)

screen = PVentana(nRES)
# ____________________________________________________________________
#/                                                                    \
#|                  /ejecutaciones de el programa\                    |
#\____________________________________________________________________/
#----------------------------------------------------------------------
Pantalla = PVentana(nRES)
aSprt = Fig_Init()
clock = PG.time.Clock()
window.mainloop()
