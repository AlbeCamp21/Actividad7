from behave import given, when, then
import re
from src.belly import Belly

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
	try:
		return float(palabra) # Cambiado a float
	except ValueError:
		numeros = {
		"cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
		"seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
		"doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
		"diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,
		"treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
		"ochenta": 80, "noventa": 90, "media": 0.5
		}
	return numeros.get(palabra.lower(), 0)

@given('que he comido {cukes:g} pepinos') # Cambiando a float
def step_given_eaten_cukes(context, cukes):
	context.belly.comer(float(cukes))

@given('que intento comer {cukes:g} pepinos')
def step_given_attempt_negative_pepinos(context, cukes):
	try:
		context.belly.comer(float(cukes))
	except Exception as e:
		context.error = str(e)

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
	time_description = time_description.strip('"').lower()
	# reemplaza 'y' o ',' por espacios
	time_description = re.sub(r'[y,]', ' ', time_description)
	time_description = time_description.strip()

	pattern = re.compile(
		r'(?:(\w+)\s*horas?)?\s*'
		r'(?:(\w+)\s*minutos?)?\s*'
		r'(?:(\w+)\s*segundos?)?'
	)

	match = pattern.match(time_description)

	if match:
		hours_word = match.group(1) or "0"
		minutes_word = match.group(2) or "0"
		seconds_word = match.group(3) or "0"

		hours = convertir_palabra_a_numero(hours_word)
		minutes = convertir_palabra_a_numero(minutes_word)
		seconds = convertir_palabra_a_numero(seconds_word)

		total_time_in_hours = hours + (minutes / 60) + (seconds/3600)
	else:
		raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")

	context.belly.esperar(total_time_in_hours)

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
	assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
	assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."
	
@then('debería ver un error')
def step_then_should_see_error(context):
	assert hasattr(context, 'error'), "Se esperaba un error"

