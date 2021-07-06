'''

Karla es una profesora de inicial muy estricta con sus alumnos. Ella quiere castigar (de alguna forma) a los niños con las calificaciones más bajas de la clase, sin embargo, ella no sabe exactamente cómo escoger a tales alumnos.
Después de pensar un buen rato, a ella se le ocurre la siguiente idea. Karla tiene  alumnos e inicialmente, tiene la lista de sus notas en un arreglo . Ella puede hacer la siguiente operación la cantidad de veces que quiera: escoger un grupo de alumnos de  y eliminar a todo alumno cuya nota sea mayor que el promedio del grupo.
Por ejemplo, si  y Karla aplica la operación al grupo , entonces ella debe eliminar de  todo alumno que tenga nota mayor a , por eso, luego de la operación el arreglo  se convierte en . Los alumnos resultantes después de todas las operaciones serán los castigados.
Tu objetivo es encontrar el número máximo de alumnos que Karla puede eliminar aplicando la operación descrita el número de veces que quiera (tal vez cero).

Input Format
La primera línea contiene un entero , el número de casos de prueba. Cada caso de prueba contiene dos líneas, la primera da un entero , el número de alumnos. La siguiente línea contiene  enteros  separados por un espacio.
Constraints


Output Format

Para cada caso de prueba, imprime un único entero, el número máximo de alumnos que Karla puede eliminar.

Sample Input 0

3
6
1 1 1 2 2 3
6
9 9 9 9 9 9
6
6 4 1 1 4 1

Sample Output 0
3
0
3


https://hackerrank-challenge-pdfs.s3.amazonaws.com/227797-la-profesora-karla-English?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1625546051&Signature=4LaLUDvqnhK59c4JS5kUssWG7A0%3D&response-content-disposition=inline%3B%20filename%3Dla-profesora-karla-English.pdf&response-content-type=application%2Fpdf
'''

nc = int(input())

for i in range (0,nc):
    n = int(input())
    ns = input()
    ab = ns.split()
    arr = []
    for x in ab:
        arr.append(int(x))
    suma = 0
    for xa in range(0,n):
        prom = int(sum(arr)) / len(arr)
        for nota in arr:
            if nota > prom:
                suma += 1
                arr.remove(nota)
    print(suma)