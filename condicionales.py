'''
hacer un algoritmo en el cual proporcione 
el divisor y tiene que darme como resultado si 
multiplo o no de ese numero
================================
entrada ::> numero a evaluar
divisor ::> numero de divisor
'''
'''
num = int(input("Ingrese Numero: "))
div = int(input("Ingrese Divisor: "))

if (num % div == 0) :
    print("El Numero ",num, "Es multiplo de ",div)
else:
    print("El Numero ",num,"NO es Multiplo de", div)
'''
#ejercicios de python usando condicionales de nivel principiante
'''

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

def calcular_imc(peso, altura):
    if altura <= 0 or peso <= 0:
        return None, "Error: Peso y altura deben ser valores positivos."
    
    imc = peso / (altura ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25.0 <= imc < 29.9:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidad"

    return imc, categoria

# Contadores para cada categoría
conteo_categorias = {
    "Bajo peso": 0,
    "Peso normal": 0,
    "Sobrepeso": 0,
    "Obesidad": 0,
}

# Procesar 5 pacientes
for i in range(1, 6):
    try:
        peso = float(input(f"Ingrese el peso del paciente {i} en kg: "))
        altura = float(input(f"Ingrese la altura del paciente {i} en metros: "))

        imc, categoria = calcular_imc(peso, altura)

        if imc is not None:
            print(f"Paciente {i}: IMC: {imc:.2f} - Categoría: {categoria}")
            conteo_categorias[categoria] += 1
        else:
            print(f"Paciente {i}: {categoria}")

    except ValueError:
        print(f"Paciente {i}: Error - Ingrese valores numéricos válidos.")

# Mostrar el resumen de categorías
print("\nResumen de categorías:")
for categoria, cantidad in conteo_categorias.items():
    print(f"{categoria}: {cantidad} pacientes")


def clasificar_imc(imc):
    if imc < 18.5:
        return "bajo_peso"
    elif 18.5 <= imc < 24.9:
        return "peso_normal"
    elif 25 <= imc < 29.9:
        return "sobrepeso"
    else:
        return "obesidad"
# Inicializamos los contadores para cada clasificación
clasificaciones = {"bajo_peso": 0, "peso_normal": 0, "sobrepeso": 0, "obesidad": 0}
# Iteramos sobre 5 pacientes con un while
i = 0
while i < 5:
    print(f"Paciente {i + 1}:")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    
    # Calculamos el IMC
    imc = peso / (altura ** 2)
    
    # Clasificamos y actualizamos el contador
    clasificacion = clasificar_imc(imc)
    clasificaciones[clasificacion] += 1
    
    i += 1
# Mostramos los resultados
print("\nResultados de la clasificación de IMC:")
for categoria, cantidad in clasificaciones.items():
    print(f"{categoria.replace('_', ' ').capitalize()}: {cantidad}")
#-----------------------------------------------------------------------------------------------------------------------------------
# Definir variables globales
totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0

def calcularimc(pesoh, alturah):
    global cBajoPeso, cPesoNormal, cSobrePeso, cObesidad  # Permitir modificar variables globales
    
    imc = pesoh / (alturah ** 2)

    if imc < 18.5:
        cBajoPeso += 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal += 1
    elif 25 <= imc < 29.9:
        cSobrePeso += 1
    else:
        cObesidad += 1

print("hola a todos")        

while totpacientes < 5:
    totpacientes += 1  
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    calcularimc(peso, altura)

# Mostrar resultados
print("\nResumen:")
print("Pacientes Bajo de Peso :", cBajoPeso)
print("Pacientes Peso Normal :", cPesoNormal)
print("Pacientes Con SobrePeso :", cSobrePeso)
print("Pacientes Con Obesidad :", cObesidad)
#--------------------------------------------------------------------------------------------------------------------------
# algoritmo con returm
def calcularimc(pesoh, alturah, cBajoPeso, cPesoNormal, cSobrePeso, cObesidad):
    imc = pesoh / (alturah ** 2)

    if imc < 18.5:
        cBajoPeso += 1
    elif 18.5 <= imc < 24.9:
        cPesoNormal += 1
    elif 25 <= imc < 29.9:
        cSobrePeso += 1
    else:
        cObesidad += 1

    return cBajoPeso, cPesoNormal, cSobrePeso, cObesidad

# Variables iniciales
totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0

print("hola a todos")        

while totpacientes < 5:
    totpacientes += 1  
    print("---------------")
    peso = float(input("Ingresa tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))

    # Actualizar los contadores con los valores devueltos
    cBajoPeso, cPesoNormal, cSobrePeso, cObesidad = calcularimc(peso, altura, cBajoPeso, cPesoNormal, cSobrePeso, cObesidad)

# Mostrar resultados
print("\nResumen:")
print("Pacientes Bajo de Peso :", cBajoPeso)
print("Pacientes Peso Normal :", cPesoNormal)
print("Pacientes Con SobrePeso :", cSobrePeso)
print("Pacientes Con Obesidad :", cObesidad)
#----------------------------------------------------------------------------------------------------------------
# validaciones ciclo While
totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0

# Lista para guardar los datos de los pacientes
pacientes = []

def calcularimc(pesoh, alturah):
    global cBajoPeso, cPesoNormal, cSobrePeso, cObesidad
    
    imc = pesoh / (alturah ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
        cBajoPeso += 1
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
        cPesoNormal += 1
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
        cSobrePeso += 1
    else:
        categoria = "Obesidad"
        cObesidad += 1
    
    return imc, categoria

print("📋 Evaluación de IMC para 5 pacientes")        

while totpacientes < 5:
    print(f"\nPaciente #{totpacientes + 1}")
    
    try:
        peso = float(input("⚖️ Ingresa tu peso en kg: "))
        if peso <= 0:
            print("⚠️ El peso debe ser mayor que 0.")
            continue

        altura = float(input("📏 Ingresa tu altura en metros: "))
        if altura <= 0:
            print("⚠️ La altura debe ser mayor que 0.")
            continue

    except ValueError:
        print("❌ Entrada inválida. Usa solo números.")
        continue

    imc, categoria = calcularimc(peso, altura)
    print(f"✅ IMC: {imc:.2f} - Categoría: {categoria}")

    pacientes.append({
        "nro": totpacientes + 1,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "categoria": categoria
    })

    totpacientes += 1

# Mostrar resumen
print("📊 Resumen:")
print("🟡 Pacientes Bajo de Peso :", cBajoPeso)
print("🟢 Pacientes Peso Normal  :", cPesoNormal)
print("🟠 Pacientes con Sobrepeso:", cSobrePeso)
print("🔴 Pacientes con Obesidad :", cObesidad)

# Mostrar todos los pacientes con su info
print("\n📁 Detalle de pacientes:")
for p in pacientes:
    print(f"Paciente {p['nro']}: ⚖️ {p['peso']} kg, 📏 {p['altura']} m, IMC: {p['imc']} → {p['categoria']}")
'''
#------------------------------------------------------------
#validacione ciclo for
# validaciones ciclo While

totpacientes = 0
cBajoPeso = 0
cPesoNormal = 0
cSobrePeso = 0
cObesidad = 0

# Lista para guardar los datos de los pacientes
pacientes = []

def calcularimc(pesoh, alturah):
    global cBajoPeso, cPesoNormal, cSobrePeso, cObesidad
    
    imc = pesoh / (alturah ** 2)

    if imc < 18.5:
        categoria = "Bajo peso"
        cBajoPeso += 1
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
        cPesoNormal += 1
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
        cSobrePeso += 1
    else:
        categoria = "Obesidad"
        cObesidad += 1
    
    return imc, categoria

print("📋 Evaluación de IMC para 5 pacientes")        

for i in range(1,6):
    print(f"\nPaciente #{i}")
    
    try:
        peso = float(input("⚖️ Ingresa tu peso en kg: "))
        if peso <= 0:
            print("⚠️ El peso debe ser mayor que 0.")
            continue

        altura = float(input("📏 Ingresa tu altura en metros: "))
        if altura <= 0:
            print("⚠️ La altura debe ser mayor que 0.")
            continue

    except ValueError:
        print("❌ Entrada inválida. Usa solo números.")
        continue

    imc, categoria = calcularimc(peso, altura)
    print(f"✅ IMC: {imc:.2f} - Categoría: {categoria}")

    pacientes.append({
        "nro": totpacientes + 1,
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "categoria": categoria
    })

    totpacientes += 1

# Mostrar resumen
print("📊 Resumen:")
print("🟡 Pacientes Bajo de Peso :", cBajoPeso)
print("🟢 Pacientes Peso Normal  :", cPesoNormal)
print("🟠 Pacientes con Sobrepeso:", cSobrePeso)
print("🔴 Pacientes con Obesidad :", cObesidad)

# Mostrar todos los pacientes con su info
print("\n📁 Detalle de pacientes:")
for p in pacientes:
    print(f"Paciente {p['nro']}: ⚖️  {p['peso']} kg, 📏 {p['altura']} m, IMC: {p['imc']} → {p['categoria']}")


print("\n📁 --------------------- Modificacion de la rama sandrarestrepo_001---------------")
x=9
y=10

def sumanumero (x,y):
    return x + y