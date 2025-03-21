from datetime import datetime
from functools import reduce  # Importamos reduce desde functools

# Lista de géneros literarios válidos (estructura inmutable, ya que es un conjunto)
generos_validos = {"Ficción", "No Ficción", "Ciencia Ficción", "Fantasía", "Misterio", "Romance", "Histórico"}

# Función pura para validar la longitud del título
def validar_longitud_titulo(titulo):
    """
    Función pura: No modifica ningún estado externo ni tiene efectos secundarios.
    Solo toma una entrada (`titulo`) y devuelve un valor booleano basado en la lógica.
    Inmutabilidad: No modifica la entrada `titulo`, solo la lee.
    """
    return 1 <= len(titulo) <= 100  # Longitud entre 1 y 100 caracteres

# Función pura para validar el año de publicación
def validar_anio_publicacion(anio):
    """
    Función pura: No modifica ningún estado externo ni tiene efectos secundarios.
    Solo toma una entrada (`anio`) y devuelve un valor booleano basado en la lógica.
    Inmutabilidad: No modifica la entrada `anio`, solo la lee.
    """
    anio_actual = datetime.now().year  # Obtiene el año actual (no modifica nada externo)
    return 1455 <= anio <= anio_actual

# Función pura para validar el género literario
def validar_genero(genero):
    """
    Función pura: No modifica ningún estado externo ni tiene efectos secundarios.
    Solo toma una entrada (`genero`) y devuelve un valor booleano basado en la lógica.
    Inmutabilidad: No modifica la entrada `genero`, solo la lee.
    """
    return genero in generos_validos  # Verifica si el género está en el conjunto de géneros válidos

# Función principal que valida todos los criterios para un libro
def validar_libro(libro):
    """
    Función pura: No modifica ningún estado externo ni tiene efectos secundarios.
    Solo toma una entrada (`libro`) y devuelve un valor booleano basado en la lógica.
    Inmutabilidad: No modifica la entrada `libro`, solo la lee.
    """
    # Usamos una tupla para almacenar los resultados de las validaciones (estructura inmutable)
    resultados = (
        validar_longitud_titulo(libro['titulo']),  # Función pura
        validar_anio_publicacion(libro['anio_publicacion']),  # Función pura
        validar_genero(libro['genero'])  # Función pura
    )
    # Retornamos True si todas las validaciones son True
    return all(resultados)  # `all` es una función pura que no modifica `resultados`

# Ejemplos de uso con datos de prueba
libros = [
    {'titulo': 'Cien años de soledad', 'anio_publicacion': 1967, 'genero': 'Ficción'},  # Válido
    {'titulo': '', 'anio_publicacion': 2020, 'genero': 'No Ficción'},  # Inválido (título vacío)
    {'titulo': '1984', 'anio_publicacion': 1949, 'genero': 'Ciencia Ficción'},  # Válido
    {'titulo': 'El Principito', 'anio_publicacion': 1400, 'genero': 'Fantasía'},  # Inválido (año fuera de rango)
    {'titulo': 'Un libro muy largo con un título que excede el límite de caracteres permitidossssssssssssssssssssssss', 'anio_publicacion': 2000, 'genero': 'Misterio'},  # Inválido (título demasiado largo)
    {'titulo': 'Rayuela', 'anio_publicacion': 1963, 'genero': 'Poesía'},  # Inválido (género no válido)
    {'titulo': 'La Odisea', 'anio_publicacion': -800, 'genero': 'Histórico'},  # Inválido (año fuera de rango)
    {'titulo': 'Futuro lejano', 'anio_publicacion': 3000, 'genero': 'Ciencia Ficción'},  # Inválido (año fuera de rango)
    {'titulo': 'Este es otro título extremadamente largo que no debería ser válido según las reglas de validación de longitud', 'anio_publicacion': 1999, 'genero': 'Fantasía'},  # Inválido (título demasiado largo)
    {'titulo': 'Crimen y castigo', 'anio_publicacion': 1866, 'genero': 'Drama'},  # Inválido (género no válido)
    {'titulo': 'El arte de la guerra', 'anio_publicacion': -500, 'genero': 'Estrategia'},  # Inválido (género no válido y año fuera de rango)
    {'titulo': '', 'anio_publicacion': 3000, 'genero': 'Biografía'},  # Inválido (título vacío, año fuera de rango, género no válido)
    {'titulo': 'Un título extremadamente largo que no cumple con las reglas de validación de longitud', 'anio_publicacion': 1400, 'genero': 'Autoayuda'},  # Inválido (título largo, año fuera de rango, género no válido)
]

# Validamos cada libro usando filter() (función pura que no modifica la lista original)
libros_validos = list(filter(validar_libro, libros))  # `filter` es una función pura
libros_no_validos = list(filter(lambda libro: not validar_libro(libro), libros))  # Libros no válidos

# Extraemos solo los títulos de los libros no válidos usando map()
titulos_validos = list(map(lambda libro: libro['titulo'],libros_validos))
titulos_no_validos = list(map(lambda libro: libro['titulo'], libros_no_validos))  # `map` para extraer títulos

# Mostramos los títulos de los libros no válidos
print("Titulos de libros validos: ",titulos_validos)
print("Títulos de libros no válidos:", titulos_no_validos)

total_libros_validos = reduce(lambda acc, _: acc + 1, libros_validos, 0)  # `reduce` para contar
total_libros_no_validos = reduce(lambda acc, _: acc + 1, libros_no_validos, 0)  # `reduce` para contar
print("Total de libros válidos:", total_libros_validos)
print("Total de libros no válidos:", total_libros_no_validos)