from pyfiglet import Figlet
import socket

# Красивый шрифт Баннера  
text = Figlet(font = 'slant')
print(text.renderText('Spektra'))

target = input("Введите IP-адрес для сканирования (Пример -> 192.168.1.1): ").strip() #Проверку не делал так что пишите правильно) 

ports = [21, 22, 80, 443, 8080] #Порты которые хотите просканировать

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Порт {port} открыт")
    else:
        print(f"[-] Порт {port} закрыт")
    sock.close()