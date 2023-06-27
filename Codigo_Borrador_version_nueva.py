import matplotlib.pyplot as plt

def grafico_barras():
    # Solicitar al usuario las categorías y valores
    categorias = input("Ingrese las categorías separadas por comas: ").split(',')
#-----------------------------------------------------------------------------------------------
    valores = [float(x) for x in input("Ingrese los valores separados por comas: ").split(',')]
    #Decimales separados por puntos ´´1.5,1.8,19´´
#-----------------------------------------------------------------------------------------------
    # Crear figura y ejes
    fig, ax = plt.subplots()
#-----------------------------------------------------------------------------------------------
    # Crear gráfico de barras con colores distintos
    colores = ['blue', 'red', 'green', 'orange', 'cyan']  
    # Puedes agregar más colores si es necesario
    ax.bar(categorias, valores, color=colores[:len(categorias)])
#-----------------------------------------------------------------------------------------------
    # Personalizar el gráfico
    ax.set_xlabel('Energia')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')
#-----------------------------------------------------------------------------------------------
    # Mostrar el gráfico
    plt.show()
#-----------------------------------------------------------------------------------------------
# Llamar a la función para generar el gráfico
grafico_barras()
