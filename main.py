from doble_list import DobleList
nombre = DobleList[str]()

nombre.append(1)
nombre.append(2)
nombre.append(3)
nombre.append(4)
nombre.travel()
print("*-*-*-*-*-*-*-*-")
nombre.eliminar_final()
nombre.travel()
print("*-*-*-*-*-*-*-*-")
nombre.eliminar_inicio()
nombre.travel()
print("*-*-*-*-*-*-*-*-")
nombre.size()

