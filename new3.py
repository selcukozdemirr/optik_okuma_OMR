import os
import pytesseract
from PIL import Image, ImageOps

# TESSDATA_PREFIX ortam değişkenini ve tesseract komut yolunu ayarlayın
os.environ['TESSDATA_PREFIX'] = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/share/tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/Library/bin/tesseract.exe'

# Görüntü yolu
image_path = 'C:/Users/Selcuk.Ozdemir/PycharmProjects/pythonProject/taramalar/tarama_Sayfa_1.jpg'

# Görüntüyü yükleyin ve ikili (binary) bir görüntüye dönüştürün
image = Image.open(image_path)
gray_image = ImageOps.grayscale(image)
binary_image = gray_image.point(lambda x: 0 if x < 128 else 255, '1')

# Öğrenci numarasını saklamak için bir dizi
student_number = []

# İlk sütunun x koordinatı ve sütunlar arası mesafe
column_start_x = 500
column_spacing = 25

# İlk satırın y koordinatı ve satırlar arası mesafe
row_start_y = 120
row_spacing = 25

# Her bir dairenin genişliği ve yüksekliği
circle_width = 15
circle_height = 15

# Eşik değeri
black_pixels_threshold = 20  # Genel eşik değerini 35 olarak ayarlıyoruz

# 24. soru için özel eşik değeri
black_pixels_threshold_24 = 80  # 24. soru için özel eşik değeri

# Her sütun ve satır için işaretlenmiş alanın yoğunluğunu kontrol edin
for col_index in range(5):  # 5 sütun için
    col = column_start_x + col_index * column_spacing
    for row_index in range(10):  # 10 rakam için
        row = row_start_y + row_index * row_spacing
        # İlgili alanı kırpın
        mark_area = binary_image.crop((col, row, col + circle_width, row + circle_height))
        # Siyah piksellerin sayısını hesaplayın
        black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
        # Eşik değerden fazla siyah piksel varsa, işaretlenmiş olarak kabul edin
        if black_pixels_count > black_pixels_threshold:
            student_number.append(str(row_index))
            break  # Bir sonraki sütuna geç

# Öğrenci numarasını birleştirin ve yazdırın
student_number = ''.join(student_number)
print(f"Öğrenci Numarası: {student_number}")

def get_column_x_for_question(question_num, column_map):
    for key, value in column_map.items():
        start, end = map(int, key.split('-'))
        if start <= int(question_num) <= end:
            return value
    raise ValueError(f"Soru numarası {question_num} için geçerli bir sütun bulunamadı.")

# BÖLÜM A ve B için soru koordinatlarını tanımlayın
answers_column_x_A = {
    '1-17': 70,
    '18-32': 300,
    '33-48': 520,
    '49-64': 748,
}
# BÖLÜM A için başlangıç y koordinatları
column_start_y_A = {
    '1-17': {'A': 510, 'B': 532},
    '18-32': {'A': 495, 'B': 518},
    '33-48': {'A': 512, 'B': 537},
    '49-64': {'A': 497, 'B': 522},
}
# A ve B seçenekleri için değişken y koordinat artışları
question_y_increments_A = {
    '1-17': [72, 82, 77, 56, 59, 68, 79, 73, 59, 63, 73, 76, 90, 110, 56, 59],
    '18-32': [77, 59, 112, 95, 86, 111, 130, 86, 74, 74, 87, 61, 60, 60],
    '33-48': [77, 74, 68, 64, 72, 70, 96, 71, 79, 78, 107, 98, 60, 64, 75],
    '49-64': [90, 66, 95, 87, 71, 56, 94, 99, 82, 58, 85, 98, 59, 65, 66]
   }
question_y_increments_B = {
    '1-17': [78, 77, 78, 54, 61, 71, 79, 69, 59, 64, 73, 76, 105, 94, 58, 57],
    '18-32': [76, 61, 111, 94, 87, 115, 127, 85, 76, 75, 85, 59, 62, 61],
    '33-48': [76, 74, 70, 61, 73, 72, 95, 70, 79, 78, 106, 99, 63, 62, 76],
    '49-64': [92, 63, 95, 87, 70, 57, 95, 98, 82, 58, 87, 97, 58, 66, 66]
}
# C seçeneği olan sorularda B ile C arasındaki mesafe
y_diff_BC = 4

# BÖLÜM B için soru koordinatları
answers_column_x_B = {'A': 1060, 'B': 1089}

# Cevapları saklamak için bir sözlük oluşturun
answers = {str(i+1): '-' for i in range(94)}



# BÖLÜM A için cevapları okuyun
current_y = 518
for question_num in range(1, 65):
    question_str = str(question_num)
    column_x = get_column_x_for_question(question_str, answers_column_x_A)
    if question_str in question_y_increments_A:
        current_y += question_y_increments_A[question_str][0]  # Burada circle_height yerine question_y_increments_A kullanılmalı
    max_black_pixels = 0
    marked_option = ''
    mark_area = binary_image.crop((column_x, current_y, column_x + circle_width, current_y + question_y_increments_A[question_str][0]))  # Burada da circle_height yerine question_y_increments_A kullanılmalı
    black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
    if black_pixels_count > max_black_pixels:
        max_black_pixels = black_pixels_count
        marked_option = 'A'
    if question_num in [20, 24, 44, 49, 60]:  # 'C' seçeneği olan sorular
        current_y += y_diff_BC
        mark_area = binary_image.crop((column_x, current_y, column_x + circle_width, current_y + question_y_increments_A[question_str][0]))  # Burada da circle_height yerine question_y_increments_A kullanılmalı
        black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
        if black_pixels_count > max_black_pixels:
            max_black_pixels = black_pixels_count
            marked_option = 'C'
    answers[question_str] = marked_option if max_black_pixels > black_pixels_threshold else '-'


# BÖLÜM B için cevapları okuyun
y_coord_B = 541
for question_num in range(65, 95):
    question_str = str(question_num)
    max_black_pixels = 0
    marked_option = ''
    for option, x_column in answers_column_x_B.items():
        mark_area = binary_image.crop((x_column, y_coord_B, x_column + circle_width, y_coord_B + circle_height))
        black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
        if black_pixels_count > max_black_pixels:
            max_black_pixels = black_pixels_count
            marked_option = option
    answers[question_str] = marked_option if max_black_pixels > black_pixels_threshold else '-'
    y_coord_B += 40

# Cevapları yazdırın
print("Cevaplar:")
for question, marked_option in answers.items():
    print(f"Soru {question}: {marked_option}")
