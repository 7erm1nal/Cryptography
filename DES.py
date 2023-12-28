import os
"""
UTF-8 Кодировка
"""
IP=(58,	50,	42,	34,	26,	18,	10,	2,
    60,	52,	44,	36,	28,	20,	12,	4,
    62,	54,	46,	38,	30,	22,	14,	6,
    64,	56,	48,	40,	32,	24,	16,	8,
    57,	49,	41,	33,	25,	17,	9,  1,
    59,	51,	43,	35,	27,	19,	11,	3,
    61,	53,	45,	37,	29,	21,	13,	5,
    63,	55,	47,	39,	31,	23,	15,	7)

reverse_IP=(40,	8,	48,	16,	56,	24,	64,	32,
            39,	7,	47,	15,	55,	23,	63,	31,
            38,	6,	46,	14,	54,	22,	62,	30,
            37,	5,	45,	13,	53,	21,	61,	29,
            36,	4,	44,	12,	52,	20,	60,	28,
            35,	3,	43,	11,	51,	19,	59,	27,
            34,	2,	42,	10,	50,	18,	58,	26,
            33,	1,	41,	9,	49,	17,	57,	25)

P= (16,	7,	20,	21,	29,	12,	28,	17,
    1,	15,	23,	26,	5,	18,	31,	10,
    2,	8,	24,	14,	32,	27,	3,	9,
    19,	13,	30,	6,	22,	11,	4,	25)

PC=(57,	49,	41,	33,	25,	17,	9,
    1,	58,	50,	42,	34,	26,	18,
    10,	2,	59,	51,	43,	35,	27,
    19,	11,	3,	60,	52,	44,	36,
    63,	55,	47,	39,	31,	23,	15,
    7,	62,	54,	46,	38,	30,	22,
    14,	6,	61,	53,	45,	37,	29,
    21,	13,	5,	28,	20,	12,	4)

reverse_PC=(14,	17,	11,	24,	1,	5,
            3,	28,	15,	6,	21,	10,
            23,	19,	12,	4,	26,	8,
            16,	7,	27,	20,	13,	2,
            41,	52,	31,	37,	47,	55,
            30,	40,	51,	45,	33,	48,
            44,	49,	39,	56,	34,	53,
            46,	42,	50,	36,	29,	32)

S=(
#S1
(
(14, 4, 13,1,	2,	15,	11,	8,	3,	10,	6,	12,	5,	9,	0,	7),
(0,	15,	 7, 4,	14,	2,	13,	1,	10,	6,	12,	11,	9,	5,	3,	8),
(4,	1, 14,  8,	13,	6,	2,	11,	15,	12,	9,	7,	3,	10,	5,	0),
(15, 12, 8,	2,	4,	9,	1,	7,	5,	11,	3,	14,	10,	0,	6,	13)
),

#S2
(
(15, 1,	8,	14,	6,	11,	3,	4,	9,	7,	2,	13,	12,	0,	5,	10),
(3,	13,	4,	7,  15,	2,	8,	14,	12,	0,	1,	10,	6,	9,	11,	5),
(0,	14,	7,	11,	10,	4,	13,	1,	5,	8,	12,	6,	9,	3,	2,	15),
(13, 8,	10,	1,	3,	15,	4,	2,	11,	6,	7,	12,	0,	5,	14,	9)
),

#S3
(
(10, 0,	9,	14,	6,	3,	15,	5,	1,	13,	12,	7,	11,	4,	2,	8),
(13, 7,	0,	9,	3,	4,	6,	10,	2,	8,	5,	14,	12,	11,	15,	1),
(13, 6,	4,	9,	8,	15,	3,	0,	11,	1,	2,	12,	5,	10,	14,	7),
(1,	10,	13,	0,	6,	9,	8,	7,	4,	15,	14,	3,	11,	5,	2,	12)
),

#S4
(
(7,	13,	14,	3,	0,	6,	9,	10,	1,	2,	8,	5,	11,	12,	4,	15),
(13, 8,	11,	5,	6,	15,	0,	3,	4,	7,	2,	12,	1,	10,	14,	9),
(10, 6,	9,	0,	12,	11,	7,	13,	15,	1,	3,	14,	5,	2,	8,	4),
(3,	15,	0,	6,	10,	1,	13,	8,	9,	4,	5,	11,	12,	7,	2,	14)
),

#S5
(
(2,	 12, 4,	1,	7,	10,	11,	6,	8,	5,	3,	15,	13,	0,	14,	9),
(14, 11, 2,	12,	4,	7,	13,	1,	5,	0,	15,	10,	3,	9,	8,	6),
(4,	 2,	 1,	11,	10,	13,	7,	8,	15,	9,	12,	5,	6,	3,	0,	14),
(11, 8,	 12, 7,	1,	14,	2,	13,	6,	15,	0,	9,	10,	4,	5,	3)
),

#S6
(
(12, 1,	 10, 15, 9,	2,	6,	8,	0,	13,	3,	4,	14,	7,	5,	11),
(10, 15, 4,	 2,	 7,	12,	9,	5,	6,	1,	13,	14,	0,	11,	3,	8),
(9,	 14, 15, 5,	 2,	8,	12,	3,	7,	0,	4,	10,	1,	13,	11,	6),
(4,	 3,	 2,	 12, 9,	5,	15,	10,	11,	14,	1,	7,	6,	0,	8,	13)
),

#S7
(
(4,	 11, 2,	 14, 15, 0,	8,	13,	3,	12,	9,	7,	5,	10,	6,	1),
(13, 0,	 11, 7,	 4,	 9,	1,	10,	14,	3,	5,	12,	2,	15,	8,	6),
(1,	 4,	 11, 13, 12, 3,	7,	14,	10,	15,	6,	8,	0,	5,	9,	2),
(6,	 11, 13, 8,	 1,	 4,	10,	7,	9,	5,	0,	15,	14,	2,	3,	12)
),

#S8
(
(13, 2,  8,	 4,	6,	15,	11,	1,	10,	9,	3,	14,	5,	0,	12,	7),
(1,	 15, 13, 8,	10,	3,	7,	4,	12,	5,	6,	11,	0,	14,	9,	2),
(7,	 11, 4,	 1,	9,	12,	14,	2,	0,	6,	10,	13,	15,	3,	5,	8),
(2,	 1,	 14, 7,	4,	10,	8,	13,	15,	12,	9,	0,	3,	5,	6,	11)
)
)

def cls():
    os.system('cls')

def bitmixer(bits:str, is_reverse:bool=False):
    """
    Выполнение начальной и конечной перестановки IP \n
    Флаг is_reverse -- конечная ли перестановка
    """
    tmp=""
    if is_reverse:
        for i in range(64):
            tmp+=bits[reverse_IP[i]-1]
        #print("Произвел конечную перестановку IP")
    else:
        for i in range(64):
            tmp+=bits[IP[i]-1]
        #print("Произвел начальную перестановку IP")
    return ''.join(tmp)

def binarystring(text:str):
    """
    Преобразует строку текста в бинарный формат
    """
    bintext=[]
    for i in range(len(text)):
        tmp=bin(ord(text[i]))[2:]
        bintext.append('0'*(8-len(tmp))+tmp)
    
    if is_verbose:
        print(*bintext, sep='\n')

    return ''.join(bintext)

def rightlenghtstr(string:str):
    """
    Добивает строку символами # до тех пор пока
    она не начнет делиться на размер блока
    """
    while len(string)%64 !=0:
        string+='0'*(8-len(bin(ord('#'))[2:]))+bin(ord('#'))[2:]
    if is_verbose:
        tmp=[string[i:i + 8] for i in range(0, len(string), 8)]
        print(*tmp, sep='\n')
    return string

def cutbinstringintoblocks(string:str):
    """
    Разделение строки битов на массив по размеру блока
    """
    tmp=[string[i:i + 64] for i in range(0, len(string), 64)]
    
    if is_verbose:
        for j in range(len(tmp)):
            b=[tmp[j][i:i + 8] for i in range(0, len(tmp[j]), 8)]
            print(*b, sep='\n')
            print('--------')

    return tmp

def charstring(string:str, flag:bool=False):
    """
    Преобразует строку битов обратно в текст
    """
    binstr=[string[i:i + 8] for i in range(0, len(string), 8)]

    text=[]
    for i in range(len(binstr)):
        text.append(chr(int(binstr[i] ,2)))
    #print("Преобразовал строку битов в текст")
    if flag:
        print(text)

    text=''.join(text)
    return text

def E(bits:str):
    """
    Расширяет 32-битный блок в 48-битный
    """
    bits=bits[-1]+bits[::]+bits[0:2]
    #расширяю строку битов с
    #1,2,3,4,5,...,29,30,31,32 до
    #32,1,2,3,4,5,...,29,30,31,32,1,2
    #И прохожу по ним блоком по 4 (от j до i) добавляя бит левее и бит правее
    tmp=[]
    j=1
    i=5
    while i<len(bits):
        tmp.append(bits[j-1]+bits[j:i]+bits[i+1])
        j+=4
        i+=4
    #print("Расширил строку с 32 до 48 битов")
    return ''.join(tmp)

def XOR(a:str, b:str):
    """
    Xor двух строк битов одинаковой длины
    0   0  =  0\n
    0   1  =  1\n
    1   0  =  1\n
    1   1  =  0\n
    Совпадающие биты дают 0, это и проверяется
    """
    tmp=''
    for i in range(len(a)):
        if a[i]!=b[i]:
            tmp+='1'
        else:
            tmp+='0'
    #print("XOR")
    return tmp

def f(string:str, key:str):
    """
    Функция Фейстеля
    """
    string=E(string) #Расширяем с 32 до 48 битов
    if is_verbose:
        print("Функция Фейстеля")
        print(*[string[i:i + 6] for i in range(0, len(string), 6)], sep='\n')
        print("Расширил половину блока текста с 32 до 48")
    bits=XOR(string, key) #XOR-им с 48-битовым ключом 
    bits=[bits[i:i + 6] for i in range(0, len(bits), 6)] #Делим на 6-битовые блоки
    if is_verbose:
        print("Сложение расширенной половины блока по модулю 2 с ключом")
        print(*bits)
    tmp=[]
    for i in range(len(bits)): #Для каждого блока:
        row=int(bits[i][0]+bits[i][-1], 2)  #Строка = крайние биты в блоке
        column=int(bits[i][1:5], 2)         #Столбец = Оставшиеся 4 бита
        a=bin(S[i][row][column])[2:]        #Подменяем на значение в соответствии с таблицей S
        tmp.append('0'*(4-len(a))+a)
        if is_verbose:
            print("Подстановка S"+str(i), "Строчка-"+str(row), "Колонка-"+str(column), "Число-"+str(a))
    if is_verbose:
        print("Результат подстановки S")
        print(*tmp)
    tmp=''.join(tmp)
    result=''
    for i in range(32):     #Конечная перестановка в функции Фейстеля
        result+=tmp[P[i]-1]
    if is_verbose:
        print("Конечная перестановка P")
        print(*[result[i:i + 4] for i in range(0, len(result), 4)], sep='\n')
        input()
    return result

def keylist(keyword:str):
    """
    Функция, генерирующая массив из 16 ключей
    """

    keyword=binarystring(keyword)
    keyword=rightlenghtstr(keyword)
    keyword=keyword[0:64]
    if is_verbose:
        print('Повторил то же самое с ключом:\nКонвертировал в бинарный формат\nДобавил символы при необходимости\nВыбрал первые 64 бита')
        print(*[keyword[i:i + 8] for i in range(0, len(keyword), 8)], sep='\n')
        input()
    K=''
    for i in range(len(PC)):            #Первичная перестановка ключа PC
        K+=keyword[PC[i]-1]
    if is_verbose:
        print('Произвел первичную перестановку ключа по таблице PC\nисключая каждый 8-й бит')
        print(*[K[i:i + 7] for i in range(0, len(K), 7)], sep='\n')
        input()
        

    C=K[0:28]
    D=K[28:]
    if is_verbose:
        print("Разделил ключ на 2 части по 28 бит")
        print(C, D, sep='\n')
        print("16 Итераций генерации ключей")
    shiftKey=1
    key=[]
    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            shiftKey=1
        else:
            shiftKey=2
        
        C=C[shiftKey:]+C[:shiftKey]
        D=D[shiftKey:]+D[:shiftKey]
        if is_verbose:
            print(i, "Левый сдвиг обоих частей на", shiftKey)
            print(C, D, sep="\n")
        result=''
        buf=C+D
        for j in range(len(reverse_PC)):            #Обратная перестановка ключа PC
            result+=buf[reverse_PC[j]-1]
        if is_verbose:
            print("Совместил обе части в одну и произвел перестановку PC2")
            print(*[result[i:i + 6] for i in range(0, len(result), 6)], sep='\n')
        key.append(result)

    return key


def Encrypt():
    """
    Главная функция шифрования
    """
    if is_verbose:
        cls()
    text=input('Введите текст:\n')
    keyword=input('Введите ключ:\n')
    if is_verbose:
        cls()
    text=binarystring(text)
    if is_verbose:
        print("Конвертировал текст в бинарный формат")
        input()
    text=rightlenghtstr(text)
    if is_verbose:
        print("Добавил символы # в конец текста для кратности с 64")
        input()
    text=cutbinstringintoblocks(text)
    if is_verbose:
        print('Разделил текст на блоки по 64 бита')
        input()

    key=keylist(keyword)
    if is_verbose:
        print('Набор из 16 ключей по 48 бит')
        print(*key, sep='\n')
        input()

    for i in range(len(text)):
        if is_verbose:
            print("Шифрование для 64-битного блока текста №"+str(i+1))

        text[i]=bitmixer(text[i])       #IP
        L=text[i][:32]      #Первая половина Left
        R=text[i][32:]      #Вторая половина Right
        
        if is_verbose:
            print(*[text[i][x:x + 8] for x in range(0, len(text[i]), 8)], sep='\n')
            print("Произвел перестановку IP\nРазделил результат надвое")
            print(L, R, sep='\n')
            input()
            print("16 Раундов шифрования")

        for j in range(16): #16 раундов
            L, R=R, XOR(L, f(R,key[j]))
            if is_verbose:
                print("Итерация", j)
                print("Левая часть", *[L[x:x + 8] for x in range(0, len(L), 8)])
                print("Правая часть", *[R[x:x + 8] for x in range(0, len(R), 8)])
                input()

        text[i]=L+R
        text[i]=bitmixer(text[i], True) #обратное IP
        if is_verbose:
            print(*[text[i][x:x + 8] for x in range(0, len(text[i]), 8)], sep='\n')
            print("64-битный блок текста после обратного IP")
            input()


    print('Символы шифротекста:')
    print(charstring(''.join(text), True))
    print('Биты шифротекста')
    print(''.join(text))

def Decrypt():
    """
    Главная функция расшифровки
    """
    if is_verbose:
        cls()
    text=input('Введите биты шифротекста:\n')
    keyword=input('Введите ключ:\n')
    if is_verbose:
        cls()
    text=rightlenghtstr(text)
    text=cutbinstringintoblocks(text)
    if is_verbose:
        print("Перевел в бинарный формат, разделил на блоки по 64 бит")
        input()
    key=keylist(keyword)
    key=key[::-1]
    if is_verbose:
        print('Набор из 16 ключей по 48 бит (в обратном порядке)')
        print(*key, sep='\n')


    for i in range(len(text)):
        if is_verbose:
            print("Расшифровка для 64-битного блока текста №"+str(i+1))
        text[i]=bitmixer(text[i])       #IP
        L=text[i][:32]      #Left
        R=text[i][32:]      #Right
        if is_verbose:
            print(*[text[i][x:x + 8] for x in range(0, len(text[i]), 8)], sep='\n')
            print("Произвел перестановку IP\nРазделил результат надвое")
            print(L, R, sep='\n')
            input()
            print("16 Раундов шифрования")
        
        for j in range(16): #16 раундов
            L, R=XOR(R, f(L,key[j])), L
            if is_verbose:
                print("Итерация", j)
                print("Левая часть", *[L[x:x + 8] for x in range(0, len(L), 8)])
                print("Правая часть", *[R[x:x + 8] for x in range(0, len(R), 8)])
                input()

        text[i]=L+R
        text[i]=bitmixer(text[i], True) #обратное IP
        if is_verbose:
            print(*[text[i][x:x + 8] for x in range(0, len(text[i]), 8)], sep='\n')
            print("64-битный блок текста после обратного IP")
            input()
    print()
    print(charstring(''.join(text)))

question=input(" Зашифровать - 0 \n Расшифровать - 1 \n")
is_verbose=input('Показать пошагово? (Y) \n')
if question=='0':
    if is_verbose == 'Y' or is_verbose == 'y':
        print('Нажимайте enter')
        input()
        is_verbose==True
        Encrypt()
    else:
        is_verbose==False
        Encrypt()
elif question=='1':
    if is_verbose == 'Y' or is_verbose == 'y':
        print('Нажимайте enter')
        input()
        is_verbose==True
        Decrypt()
    else:
        is_verbose==False
        Decrypt()
else:
    print("Не понимаю...")
    
