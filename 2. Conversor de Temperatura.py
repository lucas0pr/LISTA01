#2. Conversor de Temperatura
    # Solicite uma temperatura em Celsius.
    # Converta para Fahrenheit e Kelvin e exiba os resultados.

celsius = float (input ("Temperatura em Celsius:"))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Fahrenheit: {fahrenheit:.2f} °F")
print(f"Kelvin: {kelvin:.2f} K")
