import random
###########################################################

oyun = "Adam Asmaca"

print(oyun.center(22))

name = input("\nİsmin: ")

print(f"\nHoşgeldin {name} oynamaya hazır mısın?")

############################################################

kelimeler = ["minecraft","vscode","python","unlost","telefon","youtube","kulaklık","el","google","saat","kitap"]

gizli_kelime = random.choice(kelimeler)

tahmin_listesi = ""

lives = 10

while lives > 0:

	character_left = 0

	for character in gizli_kelime:
		if character in tahmin_listesi:
			print(character, end=' ')
		else:
			print("-", end=' ')
			character_left += 1

	if character_left == 0:
		print("\n" + name + " Kazandın!!")
		break

	tahmin = input("\nTahmin: ")

	tahmin_listesi += tahmin

	if tahmin not in gizli_kelime:
		lives -= 1
		print(f"Yanlış tahmin {lives} hakkın kaldı")

		if lives == 0:
			print(name+ " Öldün")
			print("\n"+gizli_kelime)
