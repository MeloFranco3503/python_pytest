import pytest
from ..inventario import agregar_producto, actualizar_stock, eliminar_producto, buscar_producto, inventario

def setup_function():
    # Limpia el inventario antes de cada prueba
    inventario.clear()
    
# print(inventario)

def test_agregar_producto():
    agregar_producto("Manzanas", 50, 1.50)
    assert buscar_producto("Manzanas") == {"cantidad": 50, "precio": 1.50}
    
    with pytest.raises(ValueError):
       agregar_producto("Manzanas", 30, 1.40)
       
def test_actualizar_stock():
    agregar_producto("Manzanas", 50, 1.50)
    actualizar_stock("Manzanas", 100)
    assert buscar_producto("Manzanas")["cantidad"] == 100
    
    with pytest.raises(KeyError):
        actualizar_stock("Peras", 25)
        
def test_eliminar_producto():
    agregar_producto("Manzanas", 50, 1.50)
    eliminar_producto("Manzanas")
    assert buscar_producto("Manzanas") is None
    
    with pytest.raises(KeyError):
        eliminar_producto("Peras")
        
def test_buscar_producto():
    agregar_producto("Manzanas", 50, 1.50)
    assert buscar_producto("Manzanas") == {"cantidad": 50, "precio": 1.50}
    assert buscar_producto("Peras") is None
    with pytest.raises(KeyError):
        eliminar_producto("Peras")