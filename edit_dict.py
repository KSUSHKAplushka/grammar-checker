def check_word(dictionary, word):#проверка слова в словаре 
    word = word.lower()#слово с маленькой б
    word_len = len(word)#длина слова из текста
    похожие = []#масив похожих слов
    for i in range(len(dictionary)):#проходимся по всем словам в словаре
        word_from_dict = dictionary[i].lower()#текущее слово из словоря с маленькой б
        if (len(word_from_dict) != word_len): #пропускаем,если длина не совпадает 
            continue

        letters_differ = 0 #различие букв переменая
        for i in range(word_len):
            if word[i] != word_from_dict[i]:# если различается буква
                letters_differ += 1

        if letters_differ == 0: # если нет 
            print("!", f' "{word}" ', "найдено в словаре")
            return True 

        elif letters_differ == 1 and word_len > 3: # если отличается на 1 б.,и слово больше 3
            похожие.append(word_from_dict) #вводит в массив похожие слова 

        else:
            continue

    if похожие != []:
        print(word, "похоже на", похожие) #Выводит похожие слова из словаря
    else:
        print("?", f' "{word}" ', "не найдено в словаре") #слово не найдено
    return False #этого слова нет в словаре


def main():
    f=open('word_rus.txt', encoding='utf-8')
    wordbase=f.readlines() #открыть словарь в столбик
    f.close()

    for i in range(len(wordbase)):
        wordbase[i]=wordbase[i].replace('\n','')#убрать \n

    textfile = open("sample_text.txt", encoding='utf-8')
    text = textfile.read() #открть текст на чтение 
    textfile.close()#закрыть

    raw_words = text.split(' ')
    words = []
    for i in range(len(raw_words)):
        raw_words[i]=raw_words[i].replace('.','')
        raw_words[i]=raw_words[i].replace(',','')
        raw_words[i]=raw_words[i].replace('—','')
        raw_words[i]=raw_words[i].replace('?','')
        raw_words[i]=raw_words[i].replace('"','')
        raw_words[i]=raw_words[i].replace("'",'')
        raw_words[i]=raw_words[i].replace('!','')
        raw_words[i]=raw_words[i].replace(';','')
        raw_words[i]=raw_words[i].replace(':','')
        raw_words[i]=raw_words[i].replace('«','')
        raw_words[i]=raw_words[i].replace('»','')
        raw_words[i]=raw_words[i].replace('(','')
        raw_words[i]=raw_words[i].replace(')','')
        raw_words[i]=raw_words[i].replace('0','')
        raw_words[i]=raw_words[i].replace('1','')
        raw_words[i]=raw_words[i].replace('2','')
        raw_words[i]=raw_words[i].replace('3','')
        raw_words[i]=raw_words[i].replace('4','')
        raw_words[i]=raw_words[i].replace('5','')
        raw_words[i]=raw_words[i].replace('6','')
        raw_words[i]=raw_words[i].replace('7','')
        raw_words[i]=raw_words[i].replace('8','')
        raw_words[i]=raw_words[i].replace('9','')
        raw_words[i]=raw_words[i].replace('\n', '')    
        if raw_words[i] != '':
            words.append(raw_words[i])
        

    
    for i in words:
        if check_word(wordbase, i) == False:
            print('1. ввести это слово в словарь')
            print('2. это слово с ошибкой')

            choice=input()
            if choice=='1':
                wordbase.append(i)
            if choice=='q':
                break


    f = open('word_rus.txt', 'w', encoding='utf-8')
    f.write('\n'.join(wordbase))  
     


if __name__ == "__main__":
    main()
