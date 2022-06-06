duration=int(input("Введите число в секундах: "))
# Задаем временным промежуткам переменные (как указанно в задании)
s="сек"
m="мин"
h="час"
d="дн"
# Даем условия:
    # в секундах
if duration < 60:
    print(duration, s)
    # в минутах и секундах
elif duration >= 60 and duration < 3600:
    m_min = duration // 60
    s_sec = duration % 60
    print(int(m_min), m, int(s_sec), s)
    # в часах, в минутах и секундах
elif duration >= 3600 and duration < 86400:
    h_hours = duration // 3600
    i = duration
    while i >= 3600:
        i -= 3600
    m_min = i // 60
    s_sec = duration % 60
    print(int(h_hours), h, int(m_min), m, int(s_sec), s)
    # в днях, в часах, в минутах и секундах
elif duration >= 86400:
    d_days = duration // 86400
    h_hours = (duration - 86400) // 3600
    i = duration
    while i >= 3600:
        i -= 3600
    m_min = i // 60
    s_sec = duration % 60
    print(int(d_days), d, (h_hours), h, int(m_min), m, int(s_sec), s)