#работает в папке где нужно переместить фаилы

import os, glob, shutil

class Sortingfiles(object):

	print("Что вы хотите сделать?")
	print("Копировать или создать папку?")
	def creatfolder():
		variant = input()

		if variant == "создать папку":
			while True:
				pyt = input("Введите название папки: ")
				if pyt == 'q':	break 							#выход их программы
				elif os.path.exists(pyt):
					print("Указанный файл существует")
				else:
					os.mkdir(pyt)
					print("Папка создана")


		if variant == "копировать":
			while True:
				print("Что переносим?")
				#cop = input("---")

				f_path = input("Введите название фаила фаилов - ")  #Навазние фаила, если пустая страка то все фаилы с опредленным расширением
				if f_path == 'q':    break

				new_path = input("Введите название папки куда переместить - ") #Папка куда все переместиться
				if new_path == 'q':    break

				file_extension = input("Введите расширение фаила: ")
				for txt_file in glob.glob(f_path+ f"*.{file_extension}"):
					shutil.move(txt_file, new_path)
				print("произошло копирование")

		print("Конец операции")

	creatfolder()


