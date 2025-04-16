from src.clock import convertir_tiempo_a_horas

def test_convertir_horas_simples():
	assert convertir_tiempo_a_horas("2 horas")==2.0

def test_convertir_minutos_simples():
	assert convertir_tiempo_a_horas("90 minutos")== 1.5

def test_convertir_media_hora():
	assert convertir_tiempo_a_horas("media hora")==0.5

def test_convertir_horas_y_minutos():
	assert convertir_tiempo_a_horas("1 hora y 30 minutos")==1.5

def test_convertir_horas_minutos_segundos():
	assert abs(convertir_tiempo_a_horas("2 horas, treinta minutos y treinta segundos")-2.5083) < 0.01 # Para probar si se hacen bien los cambios de unidades

def test_convertir_todo_en_palabras():
	assert abs(convertir_tiempo_a_horas("una hora y quince minutos")-1.25) < 0.01

def test_convertir_solo_segundos():
	assert abs(convertir_tiempo_a_horas("1800 segundos")-0.5) < 0.01

def test_convertir_numeros_con_texto_irregular():
	assert abs(convertir_tiempo_a_horas("dos horas treinta minutos")-2.5) < 0.01

