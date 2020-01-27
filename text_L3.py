#Считать текст из файла и выполнить последовательность действий:

print('1) методами строк очистить текст от знаков препинания;')
print()

f = open('text.txt', encoding='utf-8')
text = f.read()
str = text
symbol_list = [' ','.',',','?','!','-','–','—',"'",'"','«','»',':',';','(',')','\n']
for a in range(len(symbol_list)):
    str = str.replace(symbol_list[a],' ')
print(str)

print()
print('2) сформировать list со словами (split);')
print()

text_list = str.split()
print(text_list)

print()
print('3) привести все слова к нижнему регистру (map);')
print()

text_list = list(map(lambda x: x.lower(),text_list))
print(text_list)

print()
print('4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
print()

text_dict = {a:text_list.count(a) for a in text_list}
print(text_dict)
print()

print('5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).')
print()
sort_list = list(text_dict.items())
sort_list.sort(key = lambda i: i[1],reverse = True)
print('5 наиболее часто встречающихся слов:')
print(sort_list[:5])
text_set = set(text_list)
print('Количество разных слов в тексте:')
print(len(text_set))