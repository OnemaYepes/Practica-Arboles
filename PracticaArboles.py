
class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None



class Paciente:
  numero = 0
  def __init__(self, genero, nombre, edad, triaje):
    Paciente.numero += 1
    self.numeroPaciente = Paciente.numero
    self.genero = genero
    self.nombre = nombre
    self.edad = edad
    self.triaje = triaje

  def __str__(self):
        return (f"Paciente #{self.numeroPaciente}:\nNombre: {self.nombre}\nGénero: {self.genero}\nEdad: {self.edad}\nTriaje: {self.triaje}\n-----------------------------")


class PriorityQueue:
  def __init__(self):
    self.heap = []

  def __str__(self):
    return ' '.join(map(str, [node.value for node in self.heap]))

  def is_empty(self):
    return len(self.heap) == 0

  def insert(self, node):
    self.heap.append(node)
    self.heap_up(len(self.heap) - 1)

  def remove_min(self):
    if not self.heap:
      return 'No hay pacientes'
    else:
      min_patient = self.heap[0]
      last_patient = self.heap.pop()
      if self.heap:
        self.heap[0] = last_patient
        self.heap_down(0)
      return min_patient


  def heap_up(self, index):
    while index > 0:
      parentIndex = index // 2

      if self.heap[index].value.triaje < self.heap[parentIndex].value.triaje:
        self.heap[index], self.heap[parentIndex] = self.heap[parentIndex], self.heap[index]
        index = parentIndex
      else:
        break

  def heap_down(self, index):
    while True:
      leftchildIndex = 2 * index+1
      rightchildIndex = 2 * index+2
      root = index

      if leftchildIndex < len(self.heap) and self.heap[leftchildIndex].value.triaje < self.heap[root].value.triaje:
        root = leftchildIndex

      if rightchildIndex < len(self.heap) and self.heap[rightchildIndex].value.triaje < self.heap[root].value.triaje:
        root = rightchildIndex

      if root == index:
        break
      else:
        self.heap[index], self.heap[root] = self.heap[root], self.heap[index]
        index = root

  def get_min(self):
      if self.is_empty():
          return 'No hay pacientes para consultar'
      return self.heap[0].value

  def show_all_patients(self):
    if self.is_empty():
      print ("No hay pacientes ")
    else:
      print("Pacientes en espera:")
      for node in self.heap:
        print(node.value)

  def show_patients_triaje(self, triaje):
    hay = False
    print(f"Pacientes con triaje {triaje}:")
    for node in self.heap:
      if int(node.value.triaje) == triaje:
        print(node.value)
        hay = True
    if not hay:
      print("No hay pacientes con ese triaje")

  def detele_patient(self, nombre):
    for node in self.heap:
      if node.value.nombre == nombre:
        self.heap.remove(node)
        print("paciente eliminado exitosamente")
      else:
        print("paciente no encontrado")



priority_queue = PriorityQueue()
while True:
  print("-------------------Menú-------------------")
  print("1. Registrar un paciente")
  print("2. Consultar paciente proximo a atención")
  print("3. Atender siguiente paciente")
  print("4. Consultar los pacientes que estan en espera en general")
  print("5. Consultar los pacientes que estan en espera por triaje")
  print("6. Eliminar paciente")
  print("7. Salir")

  opcion = int(input("Seleccione una opción: "))

  if opcion == 1:
   genero = input("Ingrese el genero del paciente (Masculino/Femenino): ")
   nombre = input("Ingrese el nombre del paciente: ")
   edad = int(input("Ingrese la edad del paciente: "))
   triaje = input("Ingrese el triaje del paciente (1, 2, 3, 4, 5): ")
   paciente = Paciente(genero, nombre, edad, triaje)
   node = Node(paciente)
   priority_queue.insert(node)

  elif opcion == 2:
    paciente = priority_queue.get_min()
    print("Consulta realizada: ")
    print(paciente)

  elif opcion == 3:
    paciente = priority_queue.remove_min()
    print("atendiendo al paciente: ", paciente.value)

  elif opcion == 4:
    priority_queue.show_all_patients()

  elif opcion == 5:
    triaje = int(input("Ingrese el número de triaje (1, 2, 3, 4, 5): "))
    priority_queue.show_patients_triaje(triaje)

  elif opcion == 6:
    nombre = input("ingrese el nombre del paciente que desea eliminar: ")
    priority_queue.detele_patient(nombre)
  elif opcion == 7:
    print("Vuelva pronto.")
    break
  else:
      print("Opción inválida. Por favor, seleccione una opción válida.")