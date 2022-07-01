import datetime as dt
import locale

locale.setlocale(locale.LC_ALL, "ru") # задаем локаль для вывода даты на русском языке
dt_now = dt.datetime.now().strftime("%a: %d.%m.%y")
time_now = dt.datetime.now().strftime("%H")

