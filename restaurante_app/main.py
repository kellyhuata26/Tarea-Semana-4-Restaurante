# Archivo principal del programa

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante("Restaurante Sabor Amazónico")

# Crear productos
producto1 = Producto("Pizza Familiar", 12.50)
producto2 = Producto("Hamburguesa Especial", 7.00)
producto3 = Producto("Jugo Natural", 2.50)

# Crear clientes
cliente1 = Cliente("Kelly Huatatoca", "0991234567")
cliente2 = Cliente("Juan Pérez", "0987654321")

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_producto(producto3)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información del sistema
print("=================================")
print(" SISTEMA DE GESTIÓN DE RESTAURANTE")
print("=================================")
print(f"Nombre del restaurante: {restaurante.nombre}")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()