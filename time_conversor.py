seconds = input("Por favor, entre com o número de segundos que deseja converter: ")
total_seconds = int(seconds)

days = total_seconds // 86400
seconds_rest = total_seconds % 86400
hours = seconds_rest // 3600
seconds_left = seconds_rest % 3600
minutes = seconds_left // 60
last_seconds = seconds_left % 60

print(f"{days} dias, {hours} horas, {minutes} minutos e {last_seconds} segundos.")
