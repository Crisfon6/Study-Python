"""
APLICA UNA FUNCION A CADA ELEMETNO DE UNA LISTA ITERABLE(LISTAS,TUPLAS,ETC)
DEVOLVIENDO UNA LISTA CON LOS RESULTADOS
"""
class Empleado:
    def __init__(self, nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de $ {} ".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
Empleado("Cristhian","CEO",1000),
Empleado("Maria","CTO",800),
Empleado("Vidal","Administrativo",400),
Empleado("Cristhian","Idea",1000),
Empleado("Maria","HHHm",12331),
Empleado("Vidal","Corredor",500)
]

def calculoComision(empleado):
    if empleado.salario<1000:
        empleado.salario=empleado.salario*1.03
    return empleado

empleadosComision=map(calculoComision,listaEmpleados)

for i in empleadosComision:
    print(i)