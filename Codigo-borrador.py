#este codigo es mas para ir probando la compatibilidad entre nuestras partes del trabajo.
#----------------------------------------------------------------------
# Librerias
#----------------------------------------------------------------------
import pygame as PG, tkinter as TK, sys, math
from tkinter import ttk
#----------------------------------------------------------------------
# Constantes
#----------------------------------------------------------------------
nRES = (800, 500) ; lOk = True ; G = 10 ; LM1 = 180; COS180 = -1 
#----------------------------------------------------------------------
# Crear Pantalla Tkinter
#----------------------------------------------------------------------
window = TK.Tk()
frame = ttk.Frame(window, width=300, height=300)
frame.pack()

#----------------------------------------------------------------------
# Crear Pantalla Pygame
#----------------------------------------------------------------------
def PVentana(nRES):
    PG.init()
    ventana = PG.display.set_mode(nRES)
    nVentana  = PG.display.set_caption('simulacion')
    return ventana
#----------------------------------------------------------------------
# Mostrar por pantalla tkinter
#----------------------------------------------------------------------
#funcion
#----------------------------------------------------------------------
# caso 1
#----------------------------------------------------------------------
def caso1(m, h1, h2, dx, G, COS180):
   Emeca = m * G * h1
   Emecd = m * G * h2
   Wfnc = Emecd - Emeca
   Fr = Wfnc / (dx * COS180)

   result_text = f"Eme ca: {Emeca} J\nEme cd: {Emecd} J\nWfnc: {Wfnc} J\nFr: {Fr} N"
   result_label.config(text=result_text)
def calculate_energy():
    m = float(masa_entry.get())
    h1 = float(altura_a_entry.get())
    h2 = float(altura_d_entry.get())
    dx = float(distancia_roce_entry.get())
    caso1(m, h1, h2, dx, G, COS180
#----------------------------------------------------------------------
# caso 2
#----------------------------------------------------------------------
def caso2(altura):
   
  if    altura is None:
        
      print("Altura no proporcionada")
  elif  altura == "":
        
     print("Falta ingresar la altura")
  else:   
#----------------------------------------------------------------------
# While principal
#----------------------------------------------------------------------
ventana = PVentana(nRES)
font = PG.font.Font(None, 36)
clock = PG.time.Clock()
#----------------------------------------------------------------------
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
     
 ventana.fill((0, 255, 0))
 
 text_surface = font.render("simulacion", True, (255, 255, 255))
 text_rect = text_surface.get_rect(center=(nRES[0] // 2, nRES[1] // 2))
 ventana.blit(text_surface, text_rect)
 
 PG.display.flip()
 window.update()
 clock.tick(60)
PG.quit()
sys.exit()
