import os
import pytesseract
import tkinter as tk
from PIL import Image, ImageTk, ImageOps, ImageStat

# TESSDATA_PREFIX ortam değişkenini ayarlayın
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
circle_width = 20
circle_height = 20

# Eşik değeri
black_pixels_threshold = 60

# Öğrenci numarasını saklamak için bir dizi
student_number = []

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

# Cevapları saklamak için bir sözlük
answers = {}

#### Cevaplar için sütun x koordinatı
###answers_column_x = 70

# Her bir sütunun x koordinatlarını belirleyin
answers_column_x = {
    '1-17': 70,
    '18-32': 300,
    '33-48': 525,
    '49-64': 750,
    '65-94': 1080
}

# Soru seçeneklerinin y koordinatları
question_coords = {
    '1': {'A': 518, 'B': 541},
    '2': {'A': 590, 'B': 619},
    '3': {'A': 672, 'B': 696},
    '4': {'A': 749, 'B': 774},
    '5': {'A': 805, 'B': 828},
    '6': {'A': 864, 'B': 889},
    '7': {'A': 932, 'B': 960},
    '8': {'A': 1011, 'B': 1039},
    '9': {'A': 1084, 'B': 1108},
    '10': {'A': 1143, 'B': 1167},
    '11': {'A': 1206, 'B': 1231},
    '12': {'A': 1279, 'B': 1304},
    '13': {'A': 1355, 'B': 1380},
    '14': {'A': 1445, 'B': 1485},
    '15': {'A': 1555, 'B': 1579},
    '16': {'A': 1611, 'B': 1637},
    '17': {'A': 1670, 'B': 1694},
    '18': {'A': 495, 'B': 518},
    '19': {'A': 572, 'B': 594},
    '20': {'A': 631, 'B': 655, 'C': 684},
    '21': {'A': 743, 'B': 766},
    '22': {'A': 838, 'B': 860},
    '23': {'A': 924, 'B': 947},
    '24': {'A': 1035, 'B': 1062, 'C': 1084},
    '25': {'A': 1165, 'B': 1189},
    '26': {'A': 1251, 'B': 1274},
    '27': {'A': 1325, 'B': 1350},
    '28': {'A': 1399, 'B': 1425},
    '29': {'A': 1486, 'B': 1510},
    '30': {'A': 1547, 'B': 1569},
    '31': {'A': 1607, 'B': 1634},
    '32': {'A': 1669, 'B': 1692},
    '33': {'A': 518, 'B': 541},
    '34': {'A': 590, 'B': 619},
    '35': {'A': 672, 'B': 696},
    '36': {'A': 749, 'B': 774},
    '37': {'A': 805, 'B': 828},
    '38': {'A': 864, 'B': 889},
    '39': {'A': 932, 'B': 960},
    '40': {'A': 1011, 'B': 1039},
    '41': {'A': 1084, 'B': 1108},
    '42': {'A': 1143, 'B': 1167},
    '43': {'A': 1206, 'B': 1231},
    '44': {'A': 1279, 'B': 1304},
    '45': {'A': 1355, 'B': 1380},
    '46': {'A': 1445, 'B': 1485},
    '47': {'A': 1555, 'B': 1579},
    '48': {'A': 1611, 'B': 1637},
    '49': {'A': 1670, 'B': 1694},
    '50': {'A': 1670, 'B': 1694},
    '51': {'A': 1670, 'B': 1694},
    '52': {'A': 1670, 'B': 1694},
    '53': {'A': 1670, 'B': 1694},
    '54': {'A': 1670, 'B': 1694},
    '55': {'A': 1670, 'B': 1694},
    '56': {'A': 1670, 'B': 1694},
    '57': {'A': 1670, 'B': 1694},
    '58': {'A': 1670, 'B': 1694},
    '59': {'A': 1670, 'B': 1694},
    '60': {'A': 1670, 'B': 1694},
    '61': {'A': 1670, 'B': 1694},
    '62': {'A': 1670, 'B': 1694},
    '63': {'A': 1670, 'B': 1694},
    '64': {'A': 1670, 'B': 1694},
    '65': {'A': 518, 'B': 541},
    '66': {'A': 590, 'B': 619},
    '67': {'A': 672, 'B': 696},
    '68': {'A': 749, 'B': 774},
    '69': {'A': 805, 'B': 828},
    '70': {'A': 864, 'B': 889},
    '71': {'A': 932, 'B': 960},
    '72': {'A': 1011, 'B': 1039},
    '73': {'A': 1084, 'B': 1108},
    '74': {'A': 1143, 'B': 1167},
    '75': {'A': 1206, 'B': 1231},
    '76': {'A': 1279, 'B': 1304},
    '77': {'A': 1355, 'B': 1380},
    '78': {'A': 1445, 'B': 1485},
    '79': {'A': 1555, 'B': 1579},
    '80': {'A': 1611, 'B': 1637},
    '81': {'A': 1670, 'B': 1694},
    '82': {'A': 1670, 'B': 1694},
    '83': {'A': 1670, 'B': 1694},
    '84': {'A': 1670, 'B': 1694},
    '85': {'A': 1670, 'B': 1694},
    '86': {'A': 1670, 'B': 1694},
    '87': {'A': 1670, 'B': 1694},
    '88': {'A': 1670, 'B': 1694},
    '89': {'A': 1670, 'B': 1694},
    '90': {'A': 1670, 'B': 1694},
    '91': {'A': 1670, 'B': 1694},
    '92': {'A': 1670, 'B': 1694},
    '93': {'A': 1670, 'B': 1694},
    '94': {'A': 1670, 'B': 1694},
}


# Seçenek genişliği ve yüksekliği
option_width = 20  # Örnek genişlik
option_height = 20  # Örnek yükseklik

# Her soru ve seçenek için işaretlenmiş alanın yoğunluğunu kontrol edin
for question, options in question_coords.items():
    for option, y in options.items():
        # İlgili alanı kırpın
        mark_area = binary_image.crop((answers_column_x, y, answers_column_x + option_width, y + option_height))

        # Siyah piksellerin sayısını hesaplayın
        black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)

        # Eşik değerden fazla siyah piksel varsa, işaretlenmiş olarak kabul edin
        is_marked = black_pixels_count > black_pixels_threshold
        if is_marked:
            # İşaretlenmiş seçeneği sözlüğe ekleyin
            if question not in answers:
                answers[question] = option
            else:
                # Eğer bir soru için birden fazla işaretlenmiş seçenek varsa, bunu belirtin
                answers[question] += option

# Her soru için cevapları saklamak üzere sıralı bir sözlük oluşturun
answers = {str(i+1): '-' for i in range(10)}

# Her soru ve seçenek için işaretlenmiş alanın yoğunluğunu kontrol edin
for question, options in question_coords.items():
    max_black_pixels = 0
    marked_option = '-'
    for option, y in options.items():
        # İlgili alanı kırpın
        mark_area = binary_image.crop((answers_column_x, y, answers_column_x + option_width, y + option_height))
        # Siyah piksellerin sayısını hesaplayın
        black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
        # Eşik değerden fazla siyah piksel varsa ve mevcut maksimumdan daha fazla ise
        if black_pixels_count > black_pixels_threshold and black_pixels_count > max_black_pixels:
            max_black_pixels = black_pixels_count
            marked_option = option
    # En koyu işaretlenmiş seçeneği sözlüğe ekleyin
    answers[question] = marked_option

# Cevapları yazdırın
print("Cevaplar:")
for question, marked_option in answers.items():
    print(f"Soru {question}: {marked_option}")

