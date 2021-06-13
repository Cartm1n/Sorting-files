import os, glob, shutil

class Sortingfiles(object):

	print("Что вы хотите сделать?")
	print("Копировать или создать папку?")
	variant = input()

	if variant == "создать папку":
		pyt = ""
		while pyt != 'q':
			pyt = input("Введите путь каку папку хотите создать: ")
			if os.path.exists(pyt):
				print("Указанный файл существует")
			else:
				path = os.mkdir(pyt)

	if variant == "копировать":
		cop = ""
		while cop != 'q':
			print("Что переносим?")
			#cop = input("---")
			f_path = input("Введите название фаила фаилов - ")  #Навазние фаила, если пустая страка то все фаилы с опредленным расширением
			new_path = input("Введите название папки куда переместить - ") #Папка куда все переместиться
			for txt_file in glob.glob(f_path+"*.docx"):  #Сделать ввод расширения
				final_path = shutil.move(txt_file, new_path)
			print("произошло копирование")

	print("Конец операции")

