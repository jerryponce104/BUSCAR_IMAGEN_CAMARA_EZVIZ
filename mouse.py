import pyautogui
import time
import os

pyautogui.FAILSAFE = False

# Verificar si los archivos de imagen existen
print("Verificando la existencia de archivos de imagen...")
if not os.path.exists('cont.png'):
    print("El archivo 'cont.png' no existe en el directorio actual.")
if not os.path.exists('tri.png'):
    print("El archivo 'tri.png' no existe en el directorio actual.")

print("Iniciando búsqueda de imágenes...")
while True:
    # Intentar encontrar 'cont.png'
    try:
        ubicacion_cont = pyautogui.locateOnScreen('cont.png', confidence=0.5, grayscale=True)
        if ubicacion_cont is not None:
            print("Encontrado 'cont.png'. Realizando clic en el centro...")
            x2, y2 = pyautogui.center(ubicacion_cont)
            pyautogui.click(x2, y2)
            print(f"Realizado clic en ({x2}, {y2}).")
    except pyautogui.ImageNotFoundException:
        print("No se pudo encontrar 'cont.png'.")

    # Intentar encontrar 'tri.png'
    try:
        ubicacion_tri = pyautogui.locateOnScreen('tri.png', confidence=0.9, grayscale=True)
        if ubicacion_tri is not None:
            print("Encontrado 'tri.png'. Realizando clics...")
            clics_tri = [(105, 519), (102, 366), (110, 221)]
            for clic in clics_tri:
                pyautogui.click(clic)
                print(f"Realizado clic en {clic}.")
    except pyautogui.ImageNotFoundException:
        print("No se pudo encontrar 'tri.png'.")

    time.sleep(1)  # Tiempo de espera antes de buscar nuevamente
