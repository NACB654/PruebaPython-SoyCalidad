def mostrar_lista(productos, precios, stock):
  print("========================================")
  print("Lista de Productos " + " Precio " + " Stock")
  print("========================================")

  for i in range(0, len(productos)):
    print(f"{i + 1}" + 
          (" " * 4) + 
          f"{productos[i + 1]}" + 
          (" " * (20 - len(productos[i + 1]) - 5)) + 
          f"{precios[i + 1]}" +
          (" " * (28 - len(str(precios[i + 1])) - 20)) + 
          f"{stock[i + 1]}")

def agregar(productos, precios, stock):
  nombre = input("Ingrese el nombre del producto: ")
  precio = float(input("Ingrese su precio: "))
  cantidad = int(input("Ingrese la cantidad de stock: "))

  keys = list(productos.keys())
  nuevo_producto = keys[-1] + 1

  productos[nuevo_producto] = nombre
  precios[nuevo_producto] = precio
  stock[nuevo_producto] = cantidad

  return productos, precios, stock

def eliminar(productos, precios, stock):
  item = int(input("Ingrese el numero del item a eliminar: "))

  if len(productos) < item:
     print("Item no encontrado")
     return productos, precios, stock
  
  else:
    del productos[item]
    del precios[item]
    del stock[item]

    _productos = list(productos.values())
    _precios = list(precios.values())
    _stock = list(stock.values())
    
    productos = {i + 1 : _productos[i] for i in range(len(_productos))}
    precios = {i + 1 : _precios[i] for i in range(len(_precios))}
    stock = {i + 1 : _stock[i] for i in range(len(_stock))}

    return productos, precios, stock

def actualizar(productos, precios, stock):
  item = int(input("Ingrese el numero del item a actualizar: "))

  if len(productos) < item:
     print("Item no encontrado")
     return productos, precios, stock

  else:
    print("[1] Nombre, [2] Precio, [3] Stock")
    opcion = int(input("Elige una opcion a actualizar: "))

    while opcion > 3 or opcion < 1:
      opcion = int(input("Elige una opcion: "))

    if opcion == 1:
      cambio = input("Ingrese el cambio: ")
      productos[item] = cambio

      return productos, precios, stock
    
    elif opcion == 2:
      cambio = float(input("Ingrese el cambio: "))
      precios[item] = cambio

      return productos, precios, stock
    
    else:
      cambio = int(input("Ingrese el cambio: "))
      stock[item] = cambio

      return productos, precios, stock

def main():
  productos = {1: 'Pantalones', 2: 'Camisas', 3: 'Corbatas', 4: 'Casacas'}
  precios = {1: 200.00, 2: 120.00, 3: 50.00, 4: 350.00}
  stock = {1: 50, 2: 45, 3: 30, 4: 15}
  mostrar_lista(productos, precios, stock)

  print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
  opcion = int(input("Elige una opcion: "))

  while opcion > 4 or opcion < 1:
    opcion = int(input("Elige una opcion: "))

  if opcion == 1:
    productos, precios, stock = agregar(productos, precios, stock)
    mostrar_lista(productos, precios, stock)
    print("Producto agregado. Hasta luego.")
  elif opcion == 2:
    productos, precios, stock = eliminar(productos, precios, stock)
    mostrar_lista(productos, precios, stock)
    print("Producto eliminado. Hasta luego.")
  elif opcion == 3:
    actualizar(productos, precios, stock)
    mostrar_lista(productos, precios, stock)
    print("Producto actualizado. Hasta luego.")
  else:
    print("Hasta luego.")

if __name__ == "__main__":
  main()