inventario = {}

def agregar_producto(nombre, cantidad, precio):
    if nombre in inventario:
        raise ValueError('El producto ya existe en el inventario.')
    inventario[nombre] = {
        'cantidad': cantidad,
        'precio': precio
    }

def actualizar_stock(nombre, nueva_cantidad):
    if nombre not in inventario:
        raise KeyError('El producto no existe en el inventario.')
        
    inventario[nombre]['cantidad'] = nueva_cantidad
        

def eliminar_producto(nombre):
      if nombre not in inventario:
          raise KeyError('No existe en el inventario.')
    #   inventario.pop(nombre)
      del inventario[nombre]
      print('Producto eliminado.')
      
def buscar_producto(nombre):
    return inventario.get(nombre, None)

