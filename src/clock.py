import re

def convertir_palabra_a_numero(palabra):
	try:
		return int(palabra)
	except ValueError:
		numeros = {
			"cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
			"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
			"doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
			"diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
			"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60,
			"setenta": 70, "ochenta": 80, "noventa": 90, "media": 0.5
		}
		return numeros.get(palabra.lower(), 0)

def convertir_tiempo_a_horas(tiempo_str):
	tiempo_str = tiempo_str.strip('"').lower()
	tiempo_str = re.sub(r'[y,]', ' ', tiempo_str) # reemplaza y y comas en espacios
	tiempo_str = tiempo_str.strip()

	pattern = re.compile(
		r'(?:(\w+)\s*horas?)?\s*'
		r'(?:(\w+)\s*minutos?)?\s*'
		r'(?:(\w+)\s*segundos?)?'
	)

	match = pattern.match(tiempo_str)
	if match:
		horas = convertir_palabra_a_numero(match.group(1) or "0")
		minutos = convertir_palabra_a_numero(match.group(2) or "0")
		segundos = convertir_palabra_a_numero(match.group(3) or "0")
		return horas + (minutos / 60) + (segundos/3600)
	else:
		raise ValueError(f"No se pudo interpretar la descripción del tiempo: {tiempo_str}")

