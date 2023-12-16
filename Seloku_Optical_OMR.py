import os
import pytesseract
from PIL import Image, ImageOps

def setup_tesseract():
    # Tesseract ve ortam değişkenlerini ayarlayın
    os.environ['TESSDATA_PREFIX'] = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/share/tessdata'
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Selcuk.Ozdemir/.conda/envs/PythonProject/Library/bin/tesseract.exe'

def load_and_process_image(image_path):
    # Görüntüyü yükleyin ve işleyin
    image = Image.open(image_path)
    gray_image = ImageOps.grayscale(image)
    return gray_image.point(lambda x: 0 if x < 128 else 255, '1')

def get_student_number(image, column_start_x, column_spacing, row_start_y, row_spacing, circle_width, circle_height, black_pixels_threshold):
    student_number = []
    for col_index in range(5):  # 5 sütun için
        col = column_start_x + col_index * column_spacing
        for row_index in range(10):  # 10 rakam için
            row = row_start_y + row_index * row_spacing
            mark_area = image.crop((col, row, col + circle_width, row + circle_height))
            if sum(1 for pixel in mark_area.getdata() if pixel == 0) > black_pixels_threshold:
                student_number.append(str(row_index))
                break
    return ''.join(student_number)

def get_column_x_for_question(question_num, column_map):
    for key, value in column_map.items():
        start, end = map(int, key.split('-'))
        if start <= int(question_num) <= end:
            return value
    raise ValueError(f"Soru numarası {question_num} için geçerli bir sütun bulunamadı.")

def read_answers(image, question_coords, column_x_map, circle_width, circle_height, black_pixels_threshold):
    answers = {str(i+1): '-' for i in range(len(question_coords))}
    for question, coords in question_coords.items():
        column_x = get_column_x_for_question(question, column_x_map)
        max_black_pixels, marked_option = 0, ''
        for option, y_coord in coords.items():
            mark_area = image.crop((column_x, y_coord, column_x + circle_width, y_coord + circle_height))
            black_pixels_count = sum(1 for pixel in mark_area.getdata() if pixel == 0)
            if black_pixels_count > max_black_pixels:
                max_black_pixels, marked_option = black_pixels_count, option
        answers[question] = marked_option if max_black_pixels > black_pixels_threshold else '-'
    return answers

# Ana akış
setup_tesseract()
image_path = 'C:/Users/Selcuk.Ozdemir/PycharmProjects/pythonProject/taramalar/tarama_Sayfa_1.jpg'
binary_image = load_and_process_image(image_path)

# Öğrenci numarasını okuyun
column_start_x, column_spacing, row_start_y, row_spacing = 500, 25, 120, 25
circle_width, circle_height, black_pixels_threshold = 15, 15, 20
student_number = get_student_number(binary_image, column_start_x, column_spacing, row_start_y, row_spacing, circle_width, circle_height, black_pixels_threshold)
print(f"Öğrenci Numarası: {student_number}")

# Bölüm A için soru koordinatlarını ve sütun haritasını tanımlayın
answers_column_x_A = {
    '1-17': 70,
    '18-32': 300,
    '33-48': 520,
    '49-64': 748,
}

question_coords_A = {
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
    '31': {'A': 1607, 'B': 1631},
    '32': {'A': 1667, 'B': 1692},
    '33': {'A': 512, 'B': 537},
    '34': {'A': 589, 'B': 613},
    '35': {'A': 663, 'B': 687},
    '36': {'A': 731, 'B': 757},
    '37': {'A': 795, 'B': 818},
    '38': {'A': 867, 'B': 891},
    '39': {'A': 937, 'B': 963},
    '40': {'A': 1033, 'B': 1058},
    '41': {'A': 1104, 'B': 1128},
    '42': {'A': 1183, 'B': 1207},
    '43': {'A': 1261, 'B': 1285},
    '44': {'A': 1368, 'B': 1391, 'C': 1415},
    '45': {'A': 1466, 'B': 1490},
    '46': {'A': 1526, 'B': 1553},
    '47': {'A': 1590, 'B': 1615},
    '48': {'A': 1665, 'B': 1691},
    '49': {'A': 497, 'B': 522, 'C': 545},
    '50': {'A': 587, 'B': 614},
    '51': {'A': 653, 'B': 677},
    '52': {'A': 748, 'B': 772},
    '53': {'A': 835, 'B': 859},
    '54': {'A': 906, 'B': 929},
    '55': {'A': 962, 'B': 986},
    '56': {'A': 1056, 'B': 1081},
    '57': {'A': 1155, 'B': 1179},
    '58': {'A': 1237, 'B': 1261},
    '59': {'A': 1295, 'B': 1319},
    '60': {'A': 1380, 'B': 1406, 'C': 1430},
    '61': {'A': 1478, 'B': 1503},
    '62': {'A': 1537, 'B': 1561},
    '63': {'A': 1602, 'B': 1627},
    '64': {'A': 1668, 'B': 1693},
}

# Cevapları okuyun
answers = read_answers(binary_image, question_coords_A, answers_column_x_A, circle_width, circle_height, black_pixels_threshold)
print("Cevaplar:")
for question, marked_option in answers.items():
    print(f"Soru {question}: {marked_option}")
