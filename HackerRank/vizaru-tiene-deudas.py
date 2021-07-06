'''
 I-CPC Cusco Lima
Vizaru es un empresario muy famoso que llegó muy alto gracias a favores que ahora debe devolver. Vizaru asignó un monto de dinero a cada persona turbia con la que se relacionó y solicitó el depósito a la cuenta bancaria de cada uno de ellos sin pensarlo mucho. Al llegar a su casa, Vizaru se dio cuenta de que si estas personas se enteraban que unos recibían más que otros, harían huérfano a su hijo.
Los depósitos iniciales de Vizaru pueden verse como un arreglo  con  elementos. El banco le permite realizar una única reasignación de la siguiente forma. Vizaru puede escoger un grupo de  personas  y distribuir la cantidad  entre las  personas en total, dejando a su consideración el monto que cada uno recibe.
El número de personas  no está fijo inicialmente, es la decisión de Vizaru. Por ejemplo si  y , entonces Vizaru puede hacer la siguiente operación. Él escoge  y las personas . Luego distribuye  entre todos, quedando , (dos monedas se van para la persona ).
Nota que Vizaru no puede hacer lo mismo escogiendo  y dejar todos los montos iguales. Para cada entrada de  y , determina el mínimo valor de  para que él pueda hacer la redistribución.

Input Format

La primera línea contiene un entero , el número de casos de prueba. Cada caso de prueba contiene dos líneas, la primera da un entero , el número de personas a pagar. La siguiente línea contiene  enteros  separados por un espacio.

Constraints

Output Format

Para cada caso de prueba, imprime un único entero ; o en caso de ser la reasignación imposible, imprime  para que Vizaru pueda darse por muerto.


'''
n = int(input())
for i in range(0,n):
    n2 = int(input())
    ns = input().split()
    arr = []
    for x in ns:
        arr.append(int(x))
    suman = sum(arr)
    ideal = suman / n2
    sumas = 0
    if(not ideal.is_integer()):
        print("-1")
    else:
        for k in arr:
            if(k > ideal):
                sumas += 1
        print(sumas)