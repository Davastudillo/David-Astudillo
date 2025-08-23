# Programa para calcular promedio de calificaciones y determinar situación académica
# David Felipe Astudillo
# Introduccion a la Ingeniería de Software - Unidad 3

print("=== CALCULADORA DE PROMEDIO ACADÉMICO ===")
print("Este programa calculará su promedio final y situación académica")
print("----------------------------------------------------------------")

print("Por favor, ingresa tus 5 calificaciones:")

calificacion1 = float(input("Ingresa la calificación 1: "))
calificacion2 = float(input("Ingresa la calificación 2: "))
calificacion3 = float(input("Ingresa la calificación 3: "))
calificacion4 = float(input("Ingresa la calificación 4: "))
calificacion5 = float(input("Ingresa la calificación 5: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

print(f"\nTu promedio es: {promedio}")

if promedio >= 60:
    print("Situación académica: Aprobado")
    print("¡Felicitaciones! Has aprobado exitosamente.")
elif promedio >= 40:
    print("Situación académica: En recuperación")
    print("Debes presentar examen de recuperación.")
else:
    print("Situación académica: Reprobado")
    print("Debes repetir la materia.")

print("----------------------------------------------------------------")
print("Gracias por usar el sistema de calificaciones - David Astudillo")
