songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
how_long = sum(dict.values(songsdict))
my_spis = []
song_spis = []
song_5 = []
new_dict = songsdict.copy()
b = 0
print('Время звучания всех песен составляет:', how_long)
for i in songsdict.values():
    b +=1
    if i > 5:
        my_spis.append(b)
song_spis = list(songsdict.keys())
for i in my_spis:
    song_5.append(song_spis[i-1])
print('Вот список песен, длина которых больше 5 минут:', song_5)
for i in songsdict.keys():
    if ' ' in i:
        del new_dict[i]
    else:
        continue
print('Вот словарь из тех песен, название которых состоит из одного слова:', new_dict)


