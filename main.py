import os
from PIL import Image

def convert_images(directory):
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg"):
                filepath = subdir + os.sep + file
                try:
                    image = Image.open(filepath)
                    image.save(filepath.replace(".jpg", ".webp"), "WEBP")
                    print(f"Convertido: {filepath}")
                    os.remove(filepath)
                except:
                    print(f"Erro ao converter: {filepath}")
                    
                    
print("EX: C:/Users/User/Documentos/mangas/titulo/cap")
caminho = input("Digite o caminho para o arquivo (use o ex acima como base): ")

convert_images(caminho)
