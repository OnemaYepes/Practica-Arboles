class Node:
    __slots__ = 'value', 'next'

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

    def __str__(self):
        result = [str(x.value) for x in self]
        return ' '.join(result)


class Queue:

    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        result = [str(x.value) for x in self.linkedlist]
        return ' '.join(result)

    def is_empty(self):
        return self.linkedlist.head is None

    def enqueue(self, e):
        new_node = Node(e)
        if self.linkedlist.head is None:
            self.linkedlist.head = new_node
            self.linkedlist.tail = new_node
        else:
            new_node.next = None
            self.linkedlist.tail.next = new_node
            self.linkedlist.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return "No hay elementos en la lista"
        else:
            popped_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            popped_node.next = None
            return popped_node


class Binarytree:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data.nombre))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


def level_order(root_node):
    if not root_node:
        return "Árbol Vacío"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)

        while not custom_queue.is_empty():
            temp_root = custom_queue.dequeue()
            print(temp_root.value.data)

            if temp_root.value.leftchild is not None:
                custom_queue.enqueue(temp_root.value.leftchild)

            if temp_root.value.rightchild is not None:
                custom_queue.enqueue(temp_root.value.rightchild)


class Paciente:
  numero = 0
  def __init__(self, nombre, edad, genero, triaje):
    Paciente.numero += 1
    self.numeroPaciente = Paciente.numero
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
    self.triaje = triaje

  def __str__(self):
      return f"Paciente: #{self.numeroPaciente}, Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Triaje: {self.triaje}"


def agregar_paciente(root):
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    genero = input("Ingrese el género del paciente (femenino/masculino): ")
    triaje = input("Ingrese el triaje del paciente (1-5): ")
    paciente = Paciente(nombre, edad, genero, triaje)
    if not root.data:
        root.data = paciente
    else:
        insertar_en_arbol(root, paciente)


def adjust_heap(root):
  while root.data and root.leftchild:
      if root.rightchild and root.rightchild.data.triaje < root.leftchild.data.triaje:
          min_child = root.rightchild
      else:
          min_child = root.leftchild

      if min_child.data.triaje < root.data.triaje:
          root.data, min_child.data = min_child.data, root.data
          root = min_child
      else:
          break

def insertar_en_arbol(root, paciente):
  if paciente.triaje < root.data.triaje:
    root.data, paciente = paciente, root.data

  cola = Queue()
  cola.enqueue(root)

  while not cola.is_empty():
    temp_root = cola.dequeue().value

    if not temp_root.leftchild:
        temp_root.leftchild = Binarytree(paciente)
        adjust_heap(temp_root)
        break
    elif not temp_root.rightchild:
        temp_root.rightchild = Binarytree(paciente)
        adjust_heap(temp_root)
        break
    else:
        cola.enqueue(temp_root.leftchild)
        cola.enqueue(temp_root.rightchild)

def atender_paciente(root):
  if not root.data:
      print("No hay clientes en espera.")
      return None

  paciente_atendido = root.data

  if not root.leftchild and not root.rightchild:
      root.data = None
  else:
      ultimo_nodo = None
      cola = Queue()
      cola.enqueue(root)

      while not cola.is_empty():
          temp_root = cola.dequeue().value

          if temp_root.leftchild:
              cola.enqueue(temp_root.leftchild)
          if temp_root.rightchild:
              cola.enqueue(temp_root.rightchild)

          if not temp_root.leftchild or not temp_root.rightchild:
              ultimo_nodo = temp_root


      root.data = ultimo_nodo.data


      cola = Queue()
      cola.enqueue(root)

      while not cola.is_empty():
          temp_root = cola.dequeue().value

          if temp_root.leftchild == ultimo_nodo:
              temp_root.leftchild = None
              break
          elif temp_root.rightchild == ultimo_nodo:
              temp_root.rightchild = None
              break
          else:
              if temp_root.leftchild:
                  cola.enqueue(temp_root.leftchild)
              if temp_root.rightchild:
                  cola.enqueue(temp_root.rightchild)


  adjust_heap(root)

  return paciente_atendido

def mostrar_niveles_de_nodos(root):
  if not root.data:
    print("Árbol Vacío")
    return

  cola = Queue()
  cola.enqueue((root, 0))

  while not cola.is_empty():
    nodo_actual, nivel_actual = cola.dequeue().value
    print(f"El Paciente {nodo_actual.data.nombre} se encuentra en el nivel: {nivel_actual}")

    if nodo_actual.leftchild:
      cola.enqueue((nodo_actual.leftchild, nivel_actual + 1))
    if nodo_actual.rightchild:
      cola.enqueue((nodo_actual.rightchild, nivel_actual + 1))


def consultar_proximo_paciente(root):
  if not root.data:
    print("No hay clientes en espera.")
    return

  cola = Queue()
  cola.enqueue(root)

  while not cola.is_empty():
    nodo_actual = cola.dequeue().value
    return print(">>> Consulta paciente:\n", nodo_actual.data)

def mostrar_general(root):
  if not root.data:
    print("Árbol Vacío")
    return
  cola = Queue()
  cola.enqueue(root)
  while not cola.is_empty():
    nodo_actual = cola.dequeue().value
    print(nodo_actual.data)
    if nodo_actual.leftchild:
      cola.enqueue(nodo_actual.leftchild)
    if nodo_actual.rightchild:
      cola.enqueue(nodo_actual.rightchild)

def mostrar_pacientes_por_triaje(root, triaje_dado):
  if not root.data:
    print("Árbol Vacío")
    return

  cola = Queue()
  cola.enqueue(root)
  pacientes_encontrados = False

  while not cola.is_empty():
    nodo_actual = cola.dequeue().value

    if nodo_actual.data.triaje == triaje_dado:
      print(nodo_actual.data)
      pacientes_encontrados = True

    if nodo_actual.leftchild:
      cola.enqueue(nodo_actual.leftchild)
    if nodo_actual.rightchild:
      cola.enqueue(nodo_actual.rightchild)

  if not pacientes_encontrados:
    print(f"No se encontraron pacientes con triaje {triaje_dado}")

def eliminar_paciente_por_nombre(root, nombre):
  if not root.data:
    print("Árbol Vacío")
    return None

  if root.data.nombre == nombre:
    return eliminar_nodo(root)

  cola = Queue()
  cola.enqueue(root)

  nodo_a_eliminar = None
  ultimo_nodo = None
  ultimo_nodo_padre = None

  while not cola.is_empty():
    temp_root = cola.dequeue().value

    if temp_root.data.nombre == nombre:
      nodo_a_eliminar = temp_root

    if temp_root.leftchild:
      cola.enqueue(temp_root.leftchild)
      ultimo_nodo_padre = temp_root
      ultimo_nodo = temp_root.leftchild

    if temp_root.rightchild:
      cola.enqueue(temp_root.rightchild)
      ultimo_nodo_padre = temp_root
      ultimo_nodo = temp_root.rightchild

  if not nodo_a_eliminar:
    print("Paciente no encontrado")
    return None

  if ultimo_nodo:
    nodo_a_eliminar.data = ultimo_nodo.data
    if ultimo_nodo_padre.leftchild == ultimo_nodo:
      ultimo_nodo_padre.leftchild = None
    elif ultimo_nodo_padre.rightchild == ultimo_nodo:
      ultimo_nodo_padre.rightchild = None

  adjust_heap(root)
  return nodo_a_eliminar

def eliminar_nodo(root):
  if not root.leftchild and not root.rightchild:
    root.data = None
    return root

  ultimo_nodo = None
  ultimo_nodo_padre = None
  cola = Queue()
  cola.enqueue(root)

  while not cola.is_empty():
    temp_root = cola.dequeue().value

    if temp_root.leftchild:
      cola.enqueue(temp_root.leftchild)
      ultimo_nodo_padre = temp_root
      ultimo_nodo = temp_root.leftchild

    if temp_root.rightchild:
      cola.enqueue(temp_root.rightchild)
      ultimo_nodo_padre = temp_root
      ultimo_nodo = temp_root.rightchild

  root.data = ultimo_nodo.data
  if ultimo_nodo_padre.leftchild == ultimo_nodo:
    ultimo_nodo_padre.leftchild = None
  elif ultimo_nodo_padre.rightchild == ultimo_nodo:
    ultimo_nodo_padre.rightchild = None

  adjust_heap(root)
  return root

arbol_paciente = Binarytree(None)

while True:
  print("\nMENU:")
  print("1. Agregar persona")
  print("2. Atender paciente")
  print("3. Mostrar árbol")
  print("4. Mostrar General")
  print("5. Mostrar pacientes por triaje")
  print("6. Consultar siguiente")
  print("7. Eliminar paciente por nombre")
  print("8. Salir")
  opcion = input("Seleccione una opción: ")

  if opcion == "1":
    agregar_paciente(arbol_paciente)
    mostrar_niveles_de_nodos(arbol_paciente)
  elif opcion == "2":
    paciente_atendido = atender_paciente(arbol_paciente)
    if paciente_atendido:
      print("Cliente atendido:", paciente_atendido.nombre)
  elif opcion == "3":
    print("\nÁrbol Binario:")
    printTree(arbol_paciente)
  elif opcion == "4":
    print("\nMostrando lista general:")
    mostrar_general(arbol_paciente)
  elif opcion == "5":
    triaje_dado = input("Ingrese el número de triaje: ")
    print(f"\nPacientes con triaje {triaje_dado}:")
    mostrar_pacientes_por_triaje(arbol_paciente, triaje_dado)
  elif opcion == "6":
    consultar_proximo_paciente(arbol_paciente)
  elif opcion == "7":
    nombre_a_eliminar = input("Ingrese el nombre del paciente a eliminar: ")
    paciente_eliminado = eliminar_paciente_por_nombre(arbol_paciente, nombre_a_eliminar)
    if paciente_eliminado:
      print("Paciente eliminado:", nombre_a_eliminar)
  elif opcion == "8":
    print("¡Adiós!")
    break
  else:
    print("Opción no válida. Por favor, seleccione una opción válida.")

