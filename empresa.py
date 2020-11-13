
global listaEmpleados
listaEmpleados = list()


class Empleado(object):
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print(self.nombre,
              self.apellido,
              self.direccion,
              self.dni,
              self.antiguedad,
              self.telefono,
              self.salario,
              self.supervisor)

    def cambiarsupervisor(self, supervisor):
        supervisor = input("dime el nombre del supervisor")
        self.supervisor = supervisor
        print('supervisor cambiado')

    def incrementarsalario(self, salario=0, antiguedad=0):
        if antiguedad <= 2:
            self.salario = salario+500
        if antiguedad >= 5:
            self.salario = salario + 1000
            salario = self.salario
        print('su salario es', salario)


class Secretario(Empleado):
    despacho = ""
    rellena1 = ""

    def __init__(self,fax,puesto, nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor, despacho):
        super().__init__(nombre, apellido, dni, direccion,
                         antiguedad, telefono, salario, supervisor)
        self.despacho = despacho
        self.fax = fax
        self.puesto = puesto

    def imprimir(self):
        print("nombre:",self.nombre,
              "apellido: ",self.apellido,
              self.direccion,
              self.dni,
              self.antiguedad,
              self.telefono,
              self.salario,
              self.supervisor,
              self.despacho)

    def rellenadatos(self):
        clase =input("introduce la clase")
        clase = Empleado(
        nombre = input("nombre"),
        apellido = input("apellido"),
        dni = input("dni"),
        direccion = input("direccion"),
        antiguedad = input("antiguedad"),
        telefono = input("telefono"),
        salario = input("salario"),
        supervisor = input("supervisor"))

        listaEmpleados.append(clase)
        print()
    pass


    def imprimirEmpleados(self):
        print(listaEmpleados)
        pass

class Vendedor(Empleado):
    listClientes = list()
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor,coche,matricula,marca,modelo,telefonomovil,areadeventa,listaclientes,porcetanje):
        super().__init__(nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor)
        self.coche = coche
        self.matricula=matricula
        self.marca = marca
        self.modelo = modelo
        self.telefonomovil=telefonomovil
        self.areadeventa = areadeventa
        self.listaclientes = listaclientes
        self.porcentaje = porcetanje

    def imprimir(self):
        print(self.nombre,
              self.apellido,
              self.direccion,
              self.dni,
              self.antiguedad,
              self.telefono,
              self.salario,
              self.supervisor,
              self.coche,
              self.matricula,
              self.marca,
              self.modelo,
              self.telefonomovil,
              self.areadeventa,
              self.listaclientes,
              self.porcentaje)

    def daralta(self,nombre):
        self.listClientes.append(nombre)

    def darbaja(self,nombre):
        self.listClientes.remove(nombre)

    def incrementarsalario(self, salario=0, antiguedad=0):
         super().incrementarsalario(salario=salario, antiguedad=antiguedad)
         if antiguedad <= 2:
            self.salario = salario+500
         if antiguedad >= 5:
            self.salario = salario + 1000
            salario = self.salario
         print('su salario es', salario)
         
    pass


class Jefe_de_ventas(Empleado):
    listaVendedores = list()
    def __init__(self, nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor,secretario1,coche3,despacho,listaVendedores):
        super().__init__(nombre, apellido, dni, direccion, antiguedad, telefono, salario, supervisor)
        self.secretario1 = secretario1
        self.despacho = despacho
        self.coche = coche3
        self.listaVendedores = listaVendedores
    
    def incrementarsalario(self, salario=0, antiguedad=0):
         super().incrementarsalario(salario=salario, antiguedad=antiguedad)

    def cambiarsecretario(self,secretario1):
        self.secretario1 = secretario1
    def cambiaelcoche(self,coche):
        self.coche = coche
        print("el coche nuevo es",coche)

    def altavendedor(self,nombre):
        self.listaVendedores.append(nombre)

    def baja_vendedor(self,nombre):
        self.listaVendedores.remove(nombre)
    


if __name__ == "__main__":
    print("Bienveido al programa")

    e1 = Empleado('lara', 'gomez', 12312320,
                  'calle nueva', 5, 93244, 2000, 'Jaime')
    s1 = Secretario('juan', 'carl', 2132132320, 'calle park',
                    11, 943434, 3000, 'karl marx', '5b','Maria',5)
    v1 = Vendedor('MARIO', 'maria', 77392010,
                  'calle peña', 2, 9543212, 1000, 'Laura','seat',43434343,'bmw',800,6161263,'zaidin','listav','8%')
    j1 = Jefe_de_ventas('carla', 'dale', 7343432,
                        'calle pietro', 10, 343243432, 1200, 'juan','luis','fiat',8,'listajefe')





    v1.imprimir()
    s1.imprimir()
    s1.rellenadatos()
    s1.imprimirEmpleados()
    s1.imprimir()
