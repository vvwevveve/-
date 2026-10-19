file_path = input("введите путь к файлу: ")
parts = file_path.split("\\")

for item in parts:
    print(f"{item}")