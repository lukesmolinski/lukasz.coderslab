![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


## Zadanie 1 &ndash; Pętla `while`

W pliku `task.py` wypisz na ekran 10 razy: `I am a Python programmer`.

> Użyj pętli while.


## Zadanie 2 &ndash; Kolejne potęgi

W pliku `task.py` napisz program, który obliczy kolejne potęgi liczby 2 dla wykładnika z przedziału od 0 do 10 włącznie.

Wyświetl wynik w postaci:
```
2 to the power of 0 is 1
2 to the power of 1 is 2
2 to the power of 2 is 4
2 to the power of 3 is 8
2 to the power of 4 is 16
2 to the power of 5 is 32
2 to the power of 6 is 64
2 to the power of 7 is 128
2 to the power of 8 is 256
2 to the power of 9 is 512
2 to the power of 10 is 1024
```

> Użyj pętli `for`.


## Zadanie 3 &ndash; Porównanie imion

W pliku `task.py` napisz program, który:

* wyświetli na ekranie komunikat `Enter your name: `,
* pobierze z klawiatury imię i zapisze go do zmiennej `first_name`,
* wyświetli na ekranie komunikat `Enter your middle name: `,
* pobierze z klawiatury drugie imię użytkownika i zapisze go do zmiennej `second_name`,
* wyświetli na ekranie `Same` jeżeli imiona są takie same albo `Different` jeżeli są różne.

> Podpowiedź: użyj instrukcji warunkowej `if`!


## Zadanie 4 &ndash; Porównanie liczb

W pliku `task.py` napisz program, który przyjmie od użytkownika liczby `a` i `b`.

Wypisz informację która z nich jest większa w postaci:
```
a is greater!
```
lub
```
b is greater!
```

> Podpowiedź: pamiętaj o rzutowaniu liczb na typ liczbowy (np. `float`)!
> Stringi porównywane są z zachowaniem porządku leksykograficznego.


## Zadanie 5 &ndash; Równania kwadratowe

W pliku `task.py` napisz program, który pomoże licealistom w liczeniu pierwiastków równań kwadratowych. Program ma:

* wyświetlić na ekranie komunikat: `Equation a*x**2 + b*x + c == 0`,
* wyświetlić na ekranie komunikat: `Enter a`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `a` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Enter b`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `b` (pamiętaj o rzutowaniu na odpowiedni typ),
* wyświetlić na ekranie komunikat: `Enter c`,
* pobrać wartość od użytkownika i zapisać ją do zmiennej `c` (pamiętaj o rzutowaniu na odpowiedni typ),
* policzy deltę,
* jeśli delta > 0, policzyć wartości `x_1` i `x_2` ze wzoru:
```
x_1 = (-b - delta**0.5) / (2 * a)
x_2 = (-b + delta**0.5) / (2 * a)
```
a następnie wyświetlić je w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = <wartość>
x_2 = <wartość>
```
* jeżeli delta = 0, policzyć wartości `x_1` i `x_2` a następnie wyświetlić ją na ekranie w postaci:
```
Pierwiastki równania kwadratowego:
x_1 = x_2 = <wartość>

```
* jeżeli delta jest ujemna, wypisz na ekran `no solution`.

**Uwaga** Zakładamy, że użytkownik poprawnie poda liczby `a`, `b` i `c`.


## Zadanie 6 &ndash; Suma liczb

W pliku `task.py` napisz program, który policzy sumę wszystkich liczb od 0 do `n`, gdzie `n` jest podane przez użytkownika.

Przykład:
```
Enter n: 4
10
```


## Zadanie 7 &ndash; Średnia

W pliku `task.py` napisz program, który:
* stworzy zmienną `numbers` i przypisze do niej pustą listę,
* przyjmie od użytkownika informację, ile liczb ten chce wprowadzić i zapamięta tą informację w zmiennej `n`,
* w pętli (która wykona się `n` razy):
  * zapyta użytkownika o liczbę
  * dopisze podaną przez użytkownika liczbę na koniec listy `numbers`
* policzy ich sumę i średnią,
* wypisze na ekran te liczby oraz informację czy suma jest większa od średniej:
```
Enter n: 4
Enter a number: 1
Enter a number: 2
Enter a number: -4
Enter a number: 5
Entered numbers: 1 2 -4 5
Sum: 4,
average: 1
The sum is greater!
```


## Zadanie 8 &ndash; Definiowanie listy liczb

* Zdefiniuj listę składającą się z liczb od 1 do 8.
* Wypisz każdą z tych liczb w osobnym wierszu, poprzedzoną słowem `number: `.

Przykład:
```
number: 1
number: 2
number: 3
number: 4
number: 5
number: 6
number: 7
number: 8
```


## Zadanie 9 &ndash; Tabliczka mnożenia

W pliku `task.py` napisz program, który pobierze od użytkownika liczbę `n` (z przedziału od 1 do 10), a następnie wygeneruje działania z wynikami mnożenia podanego `n` przez liczby od 1 do 10.

##### Oczekiwany wynik:
```
Podaj liczbę: 3
1 * 3 = 3
2 * 3 = 6
3 * 3 = 9
4 * 3 = 12
5 * 3 = 15
6 * 3 = 18
7 * 3 = 21
8 * 3 = 24
9 * 3 = 27
10 * 3 = 30
```


## Zadanie 10 &ndash; Fizzbuzz

W pliku `task.py` użyj pętli `for` aby napisać program FizzBuzz. W pętli, która wykona się dla liczb z zakresu od 1 do 100 (włącznie):
* jeżeli liczba jest podzielna przez 3 i 5, wypisz na ekranie `FizzBuzz` (przykładowo dla liczby 15 ma się wypisać **tylko** `FizzBuzz`),
* jeżeli liczba jest podzielna przez 3, wypisz na ekran `Fizz`,
* jeżeli liczba jest podzielna przez 5, wypisz na ekran `Buzz`,
* w przeciwnym wypadku wypisz na ekran liczbę.

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
...
```
