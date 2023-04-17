n = int(input("Podaj liczbę całkowitą n: "))

suma = 0
for i in range(n+1):
    suma += i

print("Suma liczb od 0 do", n, "to", suma)