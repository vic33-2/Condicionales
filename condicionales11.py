duracion_de_llamada = int(input("ingresa la duracion de la llamada en minutos: "))
dia_de_la_semana = int(input("ingresa el dia de la semana (1 = martes, 8 = domingo): "))
turno = input("igresa el turno (manana/tarde): ").lower()

if duracion_de_llamada <= 4:
    costo_de_la_llamada = 1
elif duracion_de_llamada <= 8:
    costo_de_la_llamada = 1 + (duracion_de_llamada - 4) * 0.70
elif duracion_de_llamada <= 10:
    costo_de_la_llamada = 1 + 5 * 0.70 + 2 * 0.70 + (duracion_de_llamada - 8) * 0.70
else:
    costo_de_la_llamada = 1 + 5 *0.70 + 5 *0.70 + (duracion_de_llamada - 9) * 0.30

if dia_de_la_semana == 8:
    costo_de_la_llamada *= 1.04
elif turno == "tarde":
    costo_de_la_llamada *=1.13
elif turno == "manana":
        costo_de_la_llamada *=2.10

print(f"el costo de la llamada es: {costo_de_la_llamada:.2f} euros.")        