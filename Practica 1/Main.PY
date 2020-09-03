import json
import webbrowser
salir = "no" 
data = []
def funcion_salir(): 
    return "si"
def funcion_nose():
    print("Comando aceptados")
    print("1. CARGAR")
    print("2. SELECCIONAR")
    print("3. MAXIMO")
    print("4. MINIMO")
    print("5. SUMA")
    print("6. CUENTA")
    print("7. REPORTAR")
    print("8. SALIDA")       
def remove_char(s):
    return s[1 : -1]
def removechar(s):
    return s[:-1]
global table   
while (salir == "no"):  
 cadena = input("Introduce comando: ")
 salida = cadena.lower()
 if salida == "salida":
  salir = funcion_salir()
 else:
  lista = cadena.split(" ")
 if cadena == "?":
  funcion_nose()  
 comand = lista[0].lower() 
 if comand == "cargar":
  for x in range(1,len(lista)):
    if x == len(lista)-1:
      archivo = lista[x]
    else:  
     archivo = removechar(lista[x])
    with open(archivo, 'r') as f:
      if x==1:
       table = json.loads(f.read())   
      if x > 1:
       tabl = json.loads(f.read())
       for w in range(0,len(tabl)):
         table.append(tabl[w]) 
 if comand == "seleccionar":
  if lista[1] == "*":
    print("Nombre               Edad             Promedio             Activo")
    for x in range(0,len(table)):
      dicto = table[x].copy()
      print(dicto.get('nombre')+"  "+str(dicto.get('edad'))+"   "+str(dicto.get('promedio'))+"   "+str(dicto.get('activo')))
  else:
    if lista[len(lista)-3] == "nombre":
      palabra = remove_char(lista[len(lista)-1])
      for x in range(0,len(table)):
        dicciona = table[x]
        if dicciona.get('nombre') == palabra:
          for w in range(1,len(lista)-4):
            if lista[w+1] == "DONDE":
              clave = lista[w]
            else:  
              clave = removechar(lista[w])
    if lista[len(lista)-3] == "promedio":
      palabra = lista[len(lista)-1]
      for x in range(0,len(table)):
        dicciona = table[x]
        if str(dicciona.get('promedio')) == palabra:
          for w in range(1,len(lista)-4):
            if lista[w+1] == "DONDE":
              clave = lista[w]
            else:  
              clave = removechar(lista[w])
            print(clave+": "+str(dicciona.get(clave)))
    if lista[len(lista)-3] == "edad":
      palabra = lista[len(lista)-1]
      for x in range(0,len(table)):
        dicciona = table[x]
        if str(dicciona.get('edad')) == palabra:
          for w in range(1,len(lista)-4):
            if lista[w+1] == "DONDE":
              clave = lista[w]
            else:  
              clave = removechar(lista[w])
            print(clave+": "+str(dicciona.get(clave))) 
    if lista[len(lista)-3] == "activo":
      palabra = lista[len(lista)-1]
      for x in range(0,len(table)):
        dicciona = table[x]
        if str(dicciona.get('activo')).lower() == palabra.lower():
          for w in range(1,len(lista)-4):
            if lista[w+1] == "DONDE":
              clave = lista[w]
            else:  
              clave = removechar(lista[w])
            print(clave+": "+str(dicciona.get(clave)))
     
 if comand == "maximo":
   if lista[1].lower() == "edad":
     for numPasada in range(len(table)-1,0,-1):
        for i in range(numPasada):
            if table[i].get('edad')>table[i+1].get('edad'):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp  
     print("El valor maximo de edad es: "+str(table[len(table)-1].get('edad')))
   if lista[1].lower() == "promedio":
     for numPasada in range(len(table)-1,0,-1):
        for i in range(numPasada):
            if table[i].get('promedio')>table[i+1].get('promedio'):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp  
     print("El valor maximo de promedio es: "+str(table[len(table)-1].get('promedio')))
 if comand == "minimo":
   if lista[1].lower() == "edad":
     for numPasada in range(len(table)-1,0,-1):
        for i in range(numPasada):
            if table[i].get('edad')<table[i+1].get('edad'):
                temp = table[i]
                table[i] = table[i+1]
                table[i+1] = temp  
     print("El valor minimo de edad es: "+str(table[len(table)-1].get('edad')))
   if lista[1].lower() == "promedio":
    for numPasada in range(len(table)-1,0,-1):
      for i in range(numPasada):
          if table[i].get('promedio')<table[i+1].get('promedio'):
             temp = table[i]
             table[i] = table[i+1]
             table[i+1] = temp  
    print("El valor minimo de promedio es: "+str(table[len(table)-1].get('promedio')))
 if comand == "suma":
   suma = 0
   if lista[1].lower() == "promedio":
     for x in range(0,len(table)):
       suma = suma + table[x].get('promedio')
     print("El total de promedio es: "+str(suma))
   if lista[1].lower() == "edad":
     for x in range(0,len(table)):
       suma = suma + table[x].get('edad')
     print("El total de edad es: "+str(suma))
 if comand == "cuenta":
   total = len(table)
   print("El numero de registros existentes es: "+str(total))
 if comand == "reportar":
   if int(lista[1]) > (len(table)):
     print("error 101")
   else: 
     f = open('reporte.html','wb')
     mensaje = """<html>
     <head><title>Reporte</title></head>
     <body>
     <h2 align="center">Reporte de elementos</h2>
     <div style="text-align:center;">
	   <table border="1" style="margin: 0 auto;">
		 <tr>
		 <td>Nombre</td>
     <td>Edad</td>
     <td>Promedio</td>
     <td>Activo</td>
	   </tr>"""
     mensajefinal ="""</table>
     </div>
     </body>
     </html>"""   
     for x in range(0,int(lista[1])):
      mensaje = mensaje + "<tr> <td> "+table[x].get('nombre')+"</td> <td> "+str(table[x].get('edad'))+"</td> <td> "+str(table[x].get('promedio'))+"</td> <td> "+str(table[x].get('activo'))+"</td></tr>"
     mensaje = mensaje + mensajefinal
     f.write(bytes(mensaje,"ascii"))
     f.close()
     webbrowser.open_new_tab('reporte.html')
