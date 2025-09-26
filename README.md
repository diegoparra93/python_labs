## Python Labs
[Python Lab01](/README_files/lab01_readme.md)


Задание 1

nombre = input("Имя: ")
edad = int(input("Возраст: "))
print(f"Привет, {nombre}! Через год тебе будет {edad + 1}.")

![alt](images/lab01/01.png)

Задание 2

a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
sum_ = a + b
avg_ = sum_ / 2
print(f"sum={sum_:.2f}; avg={avg_:.2f}")

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/02.png?raw=true)


Задание 3

price = 1000.0
discount = 15.0
vat = 20.0

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"Precio inicial: {price:.2f} ₽")
print(f"Descuento: {discount:.2f}%")
print(f"Base después del descuento: {base:.2f} ₽")
print(f"IVA ({vat:.2f}%): {vat_amount:.2f} ₽")
print(f"Total a pagar: {total:.2f} ₽")

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/03.png)

Задание 4

# src/04_minutes_to_hhmm.py
# Ask user for minutes
minutes = int(input("Minutes: "))
# Calculate hours and minutes
hours = minutes // 60
remaining_minutes = minutes % 60
# Display in HH:MM format
print(f"{hours}:{remaining_minutes:02d}")
![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/04.png)

Задание 5

fio = input().strip()  
palabras = fio.split()  
inic = ''
for palabra in palabras:
    if palabra:  
        inic += palabra[0].upper()  
len_ = len(fio)  
print(f"ФИО: {fio}")
print(f"Инициалы: {inic}.")
print(f"Длина (символов): {len_}")
![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/05.png)

Задание 6

n = int(input())
ochn = 0
zaochn = 0
for i in range(n):
    name = input().split()
    if 'True' in name:
        ochn += 1
    else:
        zaochn += 1
print(ochn, zaochn)
![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/06.png)

Задание 7

str_ = str(input())

newstr_ = ''
index_first = -1
index_second = -1
index_last = -1

for i in str_:
    index_first += 1
    if i.isupper():
        break

for i in range(len(str_) - 1):
    if str_[i].isdigit():
        index_second = i + 1
        break

for i in str_:
    index_last += 1
    if i == '.':
        break
        

shag = index_second - index_first

for i in range(index_first, index_last + 1, shag):
    newstr_ += str_[i]
print(newstr_)
![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/07.png)
