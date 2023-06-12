
import matplotlib.pyplot as plt

def grafico_barras():
    # Solicitar al usuario las categorías y valores
    categorias = input("Ingrese las categorías separadas por comas: ").split(',')
    valores = [int(x) for x in input("Ingrese los valores separados por comas: ").split(',')]
    
    # Crear figura y ejes
    fig, ax = plt.subplots()
    
    # Crear gráfico de barras
    ax.bar(categorias, valores)
    
    # Personalizar el gráfico
    ax.set_xlabel('Categorías')
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico de Barras')
    
    # Mostrar el gráfico
    plt.show()

# Llamar a la función para generar el gráfico
grafico_barras()


