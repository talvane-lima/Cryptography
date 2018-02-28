#coding: utf-8
def cifrador_cesar(texto, key=1):
	texto_cifrado = ""
	for n in texto:
		if n < 'a' or n > 'z':
			texto_cifrado += n
			continue
		if n == 'z':
			texto_cifrado += 'a'
		else:
			texto_cifrado += chr(ord(n) + key)
	return texto_cifrado
file = open('pt-BR.dic', 'r')
aux_dic = file.read().split("\n")

dic = []
for n in aux_dic:
	dic.append(n.split("/")[0].replace('á', "a").replace('ã', "a").replace('à', "a").replace('â', "a").replace('é', "e").replace('ê', "e").replace('í', "i").replace('ó', "o").replace('ô', "o").replace('õ', "o").replace('ú', "u").replace('ç', "c").lower())

dic_string = "".join(dic)

count_dic = {}

letter = ord('a')

while chr(letter) != 'z':
	count_dic.update({chr(letter):dic_string.count(chr(letter))})
	letter += 1

import operator
count_dic = sorted(count_dic.items(), key=operator.itemgetter(1))[::-1]

file = open('texto.txt', 'r')

texto = file.read().replace('á', "a").replace('ã', "a").replace('à', "a").replace('â', "a").replace('é', "e").replace('ê', "e").replace('í', "i").replace('ó', "o").replace('ô', "o").replace('õ', "o").replace('ú', "u").replace('ç', "c").lower()

count_dic_texto = {}

letter = ord('a')
texto_cifrado = cifrador_cesar(texto)
while chr(letter) != 'z':
	count_dic_texto.update({chr(letter):texto_cifrado.count(chr(letter))})
	letter += 1

count_dic_texto = sorted(count_dic_texto.items(), key=operator.itemgetter(1))[::-1]

output = []


for i in range(27):
	texto_cifrado = cifrador_cesar(texto_cifrado)
	print texto_cifrado