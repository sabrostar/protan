import random
import time
import win32api
import win32con
import cv2
import numpy as np
from windowcapture import WindowCapture


# Görüntü yakalamak için OpenCV kullanımı
def find_image_on_screen(image_path, threshold=0.8):
    # Ekran görüntüsü al
    screen = np.array(WindowCapture().get_screenshot())
    # Görseli oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntü eşleştirmeyi yap
    result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    # Eşleşen koordinatları döndür
    locations = list(zip(*locations[::-1]))
    return locations


# Win32 API kullanarak fareyi hareket ettirme ve tıklama işlemi
def move_mouse(x, y):
    win32api.SetCursorPos((x, y))


def click_mouse(x, y):
    move_mouse(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y)


# Tuş basma işlemleri için Win32 API
def press_key(key, min_delay=0.1, max_delay=0.5):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(min_delay=min_delay, max_delay=max_delay)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


# Uyuma fonksiyonu
def sleep(min_delay=0.1, max_delay=0.5):
    if min_delay > max_delay:
        min_delay, max_delay = max_delay, min_delay
    time.sleep(random.uniform(min_delay, max_delay))


# Portal tıklama işlemi
def portal_tiklama():
    locations = find_image_on_screen("protean.png")
    if locations:
        x, y = locations[0]
        click_mouse(x + 5, y + 410)
        sleep(min_delay=0.1, max_delay=0.2)
        press_key(key=w)
        sleep(min_delay=2, max_delay=3)
        press_key(key=f)


def proteanbasma():
    press_key(key=Z)
    sleep(min_delay=0.1, max_delay=0.3)
    press_key(key=R)
    sleep(min_delay=0.2, max_delay=0.3)
    press_key(key=ONE)

    press_key(key=Z)
    sleep(min_delay=0.1, max_delay=0.3)
    press_key(key=R)
    sleep(min_delay=0.2, max_delay=0.3)
    press_key(key=ONE)

    press_key(key=Z)
    sleep(min_delay=0.1, max_delay=0.3)
    press_key(key=R)
    sleep(min_delay=0.2, max_delay=0.3)
    press_key(key=ONE)
    sleep(min_delay=2.1, max_delay=3.9)

    pyautogui.moveTo(tp1_konumx + 0, tp1_konumy - 0)
    sleep(min_delay=0.1, max_delay=0.2)
    click_mouse(tp1_konumx + 0, tp1_konumy - 0)


# Diğer tıklama ve basma işlemleri de benzer şekilde aynı mantıkla `win32api` ve OpenCV ile yapılabilir.
# ...


def kasmabaslasin():
    proteanbasma()
    sleep(min_delay=0.1, max_delay=0.2)
    portal_tiklama()
    sleep(min_delay=0.1, max_delay=0.2)
    tarroncamp_tiklama()
    sleep(min_delay=0.1, max_delay=0.2)
    tarroncampbasma()
    sleep(min_delay=0.1, max_delay=0.2)
    portal_tiklama()
    sleep(min_delay=0.1, max_delay=0.2)
    siena_tiklama()
    sleep(min_delay=0.1, max_delay=0.2)
    sienabasma()
    sleep(min_delay=0.1, max_delay=0.2)


while True:
    try:
        kasmabaslasin()
        sleep(min_delay=0.1, max_delay=0.2)
    except Exception as e:
        print(f"Error: {e}")
        pass