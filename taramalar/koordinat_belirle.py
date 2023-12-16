import os
import pytesseract
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageStat

# TESSDATA_PREFIX ortam değişkenini ayarlayın
os.environ['TESSDATA_PREFIX'] = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/share/tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/Library/bin/tesseract.exe'

# Görüntü yolu
image_path = 'C:/Users/Selcuk.Ozdemir/PycharmProjects/pythonProject/taramalar/tarama_Sayfa_1.jpg'

# Koordinatları saklamak için liste
coords = []

# Fare olayı için başlangıç koordinatları
start_x, start_y = None, None

# Fare olayı için bitiş koordinatları
end_x, end_y = 0, 0

# Mouse callback fonksiyonu
def mouse_press(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def mouse_drag(event):
    global start_x, start_y
    if start_x is None or start_y is None:
        start_x, start_y = event.x, event.y
    else:
        end_x, end_y = event.x, event.y
        dx, dy = end_x - start_x, end_y - start_y
        canvas.move(image_id, dx, dy)
        update_coords(dx, dy)
        start_x, start_y = end_x, end_y

def mouse_release(event):
    global start_x, start_y, end_x, end_y
    start_x, start_y = None, None
    end_x, end_y = 0, 0

def update_coords(dx, dy):
    global coords
    new_coords = []
    for coord in coords:
        x1, y1, x2, y2 = coord
        x1 += dx
        y1 += dy
        x2 += dx
        y2 += dy
        new_coords.append((x1, y1, x2, y2))
    coords = new_coords

# Tkinter penceresi oluşturun
root = tk.Tk()
root.title("Görüntü Taşıma ve Kaydırma")

# Scrollbar'ı oluşturun
vsb = ttk.Scrollbar(root, orient="vertical")
vsb.pack(side="right", fill="y")

# Canvas (çizim alanı) oluşturun ve görüntüyü ekleyin
canvas = tk.Canvas(root, width=800, height=600, yscrollcommand=vsb.set)
canvas.pack()

# Görüntüyü yükleyin ve PhotoImage nesnesi oluşturun
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Görüntüyü canvas üzerine ekleyin
image_id = canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Canvas'ı kaydırılabilir hale getirin
vsb.config(command=canvas.yview)

# Fare olaylarını bağlayın
canvas.bind("<ButtonPress-1>", mouse_press)
canvas.bind("<B1-Motion>", mouse_drag)
canvas.bind("<ButtonRelease-1>", mouse_release)

# İptal etmek için 'q' tuşuna basılmasını bekleyin
def exit_program(event):
    if event.keysym == "q":
        root.destroy()

root.bind("<Key>", exit_program)

# Pencereyi gösterin
root.mainloop()

# Koordinatları yazdır
print(f"Tüm koordinatlar: {coords}")

# Sabit sütun ve satır hizaları
column_start_x = 75  # Sabit sütun hizası
row_spacing = 20     # Her satır arasındaki sabit yükseklik

# Seçeneklerin kaçıncı çizgiye denk geldiğini hesaplayın
def calculate_coordinates(option_number):
    row = option_number * row_spacing  # Satır hizası hesaplama
    column = column_start_x           # Sabit sütun hizası
    return column, row

# Örnek: 3. seçeneğin koordinatlarını alın
option_number = 3
column, row = calculate_coordinates(option_number)
print(f"Seçenek {option_number} koordinatları: ({column}, {row})")