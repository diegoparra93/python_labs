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