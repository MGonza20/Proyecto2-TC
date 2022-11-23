
cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))
cuatro = lambda f: lambda x: f(f(f(f(x))))
cinco = lambda f: lambda x: f(f(f(f(f(x)))))
seis = lambda f: lambda x: f(f(f(f(f(f(x))))))
siete = lambda f: lambda x: f(f(f(f(f(f(f(x)))))))
ocho = lambda f: lambda x: f(f(f(f(f(f(f(f(x))))))))
nueve = lambda f: lambda x: f(f(f(f(f(f(f(f(f(x)))))))))
diez = lambda f: lambda x: f(f(f(f(f(f(f(f(f(f(x))))))))))

sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)

print("Alpha")
# Deben ser iguales
print("Sucesor")
print(sucesor(uno)(lambda x: x + 1)(1))
print(dos(lambda x: x + 1)(1))

# Deben ser iguales
print(sucesor(cuatro)(lambda x: x + 1)(1))
print(cinco(lambda x: x + 1)(1))


print("Suma")
# Deben de ser iguales
print(suma(uno)(tres)(lambda x: x + 1)(1))
print(cuatro(lambda x: x + 1)(1))

# Deben de ser iguales
print(suma(cinco)(cuatro)(lambda x: x + 1)(1))
print(nueve(lambda x: x + 1)(1))

print("Multiplicacion")

# Deben ser iguales
print(multiplicacion(dos)(uno)(lambda x: x + 1)(1))
print(dos(lambda x: x + 1)(1))

# Deben ser iguales
print(multiplicacion(tres)(tres)(lambda x: x + 1)(1))
print(nueve(lambda x: x + 1)(1))

print("Potencia")

# Deben de ser iguales
print(potencia(uno)(cero)(lambda x: x + 1)(1))
print(uno(lambda x: x + 1)(1))

# Deben de ser iguales
print(potencia(dos)(tres)(lambda x: x + 1)(1))
print(ocho(lambda x: x + 1)(1))


# Beta
print("Beta")
# Deben ser iguales
print("Sucesor")
print(sucesor(uno)(lambda x: x * 2)(1))
print(dos(lambda x: x * 2)(1))

# Deben ser iguales
print(sucesor(cuatro)(lambda x: x * 2)(1))
print(cinco(lambda x: x * 2)(1))

print("Suma")

# Deben de ser iguales
print(suma(uno)(tres)(lambda x: x * 2)(1))
print(cuatro(lambda x: x * 2)(1))

# Deben de ser iguales
print(suma(cinco)(cuatro)(lambda x: x * 2)(1))
print(nueve(lambda x: x * 2)(1))

# Deben ser iguales
print(multiplicacion(dos)(uno)(lambda x: x * 2)(1))
print(dos(lambda x: x * 2)(1))
print("Multiplicacion")

# Deben ser iguales
print(multiplicacion(tres)(tres)(lambda x: x * 2)(1))
print(nueve(lambda x: x * 2)(1))


print("Potencia")
# Deben de ser iguales
print(potencia(uno)(cero)(lambda x: x * 2)(1))
print(uno(lambda x: x * 2)(1))

# Deben de ser iguales
print(potencia(dos)(tres)(lambda x: x * 2)(1))
print(ocho(lambda x: x * 2)(1))

