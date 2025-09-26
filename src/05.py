fio = input().strip()  # strip() quita espacios al inicio y final
palabras = fio.split()  # split() divide en palabras

inic = ''
for palabra in palabras:
    if palabra:  # Si la palabra no está vacía
        inic += palabra[0].upper()  # Primera letra en mayúscula

len_ = len(fio)  # Longitud SIN espacios finales (gracias al strip())

print(f"ФИО: {fio}")
print(f"Инициалы: {inic}.")
print(f"Длина (символов): {len_}")