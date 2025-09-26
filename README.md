## Python Labs
[Python Lab01](/README_files/lab01_readme.md)


Задание 1

```
name = input()
age = int(input())
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

![alt](images/lab01/01.png)

Задание 2

```
a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
sum_ = a + b
avg_ = sum_ / 2
print(f"sum={sum_:.2f}; avg={avg_:.2f}")
```

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/02.png?raw=true)


Задание 3

```
price = int(input())
discount = int(input())
vat = int(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} $")
print(f"Ндс              : {vat_amount:.2f} $")
print(f"Итого к оплате   : {total:.2f} $")
```

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/03.png)

Задание 4
```
m = int(input())

hours = m // 60
minutes = m % 60

print(f"{hours}:{minutes:02d}")

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/04.png)
```
Задание 5
```
fio_input = input()
fio_new = ' '.join(fio_input.split())

words = fio_new.split()

initials = ''.join([word[0].upper() for word in words])

length = len(fio_new)

print(f"ФИО             : {fio_input}")
print(f"Инициалы        : {initials}.")
print(f"Длина (символов): {length}")

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/05.png)
```
Задание 6
```
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
```

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/06.png)

Задание 7
```
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
```

![alt](https://github.com/diegoparra93/python_labs/blob/main/images/lab01/07.png)
