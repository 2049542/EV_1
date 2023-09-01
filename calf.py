##pregunta al alumno 5 de sus calificaciones y obten el promedio
nombre= input("Escribe el nombre del alumno. ")
calf1=float(input("Escribe la clificacion final de Quimica. "))
calf2=float(input("Escribe la clificacion final de Matematicas. "))
calf3=float(input("Escribe la clificacion final de Español. "))
calf4=float(input("Escribe la clificacion final de Artes. "))
calf5=float(input("Escribe la clificacion final de Programacion. "))
operacion=int (calf1 + calf2 + calf3 + calf4 + calf5) / 5
print ("El promedio de " + str (nombre) + " es de: " + str (operacion))