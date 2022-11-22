


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

# numbers = {
# 	0: cero,
# 	1: uno,
# 	2: dos,
# 	3: tres,
# 	4: cuatro,
# 	5: cinco,
# 	6: seis,
# 	7: siete,
# 	8: ocho,
# 	9: nueve,
# 	10: diez
# }


sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)
# suma = lambda a, b: numbers[a+b]
# multiplicacion = lambda a,b: numbers[a*b]
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)

print(multiplicacion(dos)(uno)(lambda x: x + 1)(1))