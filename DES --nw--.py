def binarystring(text:str):
    """
    Преобразует строку текста в бинарный формат
    """
    bintext=[]
    for i in range(len(text)):
        tmp=bin(ord(text[i]))[2:]
        bintext.append('0'*(sizeOfChar-len(tmp))+tmp)
    return ''.join(bintext)

def rightlenghtstr(string:str):
    """
    Добивает строку символами # до тех пор пока
    она не начнет делиться на размер блока
    """
    while len(string)%sizeOfBlock !=0:
        string+='0'*(sizeOfChar-ord('#'))+bin(ord('#'))[2:]
    return string

def cutbinstringintoblocks(string:str):
    """
    Разделение строки битов на массив по размеру блока
    """
    tmp=[string[i:i + sizeOfBlock] for i in range(0, len(string), sizeOfBlock)]
    return tmp

def charstring(string:str):
    """
    Преобразует строку битов обратно в текст
    """
    binstr=[string[i:i + sizeOfChar] for i in range(0, len(string), sizeOfChar)]
    text=[]
    for i in range(len(binstr)):
        text.append(chr(int(binstr[i] ,2)))
    return ''.join(text)

def LengthKeyword(text:str, kwLength:int):
    """
    Отрезает лишнее от ключа или добавляет нули в начало
    """
    if len(text)>kwLength:
        text=text[0:kwLength]
    else:
        while len(text)<kwLength:
            text='0'+text
    return text

def XOR(a:str,b:str):
    """
    xor...просто xor...
    """
    result=''
    for i in range(len(a)):
        if a[i]==b[i]:
            result+=('0')
        else:
            result+=('1')
    return result

def f(a:str,b:str):
    """
    Шифрующая функция
    """
    return XOR(a,b) #Позже изменю

def DecodeRound(string:str, key:str):
    L=string[0:len(string)/2]
    R=string[len(string)/2:]

    return XOR(f(L, key), R)+L

def EncodeRound(string:str, key:str):
    L=string[0:len(string)/2]
    R=string[len(string)/2:]

    return R+XOR(L,f(R,key))

def shiftkey_next(key:str):
    """
    Сдвиг ключа на указанное кол-во символов \n
    сло[во]-[во]сло
    """
    key=key[len(key)-shiftKey:]+key[:len(key)]
    return key

def shiftKey_prev(key:str):
    """
    Сдвиг ключа на указанное кол-во символов \n
    [сл]ово-ово[сл]
    """
    key=key[shiftKey:]+key[:shiftKey]
    return key


sizeOfBlock=128
sizeOfChar=16
shiftKey=2
quantityOfRounds=16 

text=input("Введите текст для шифрования \n")
key=input("Введите ключ\n")

text=rightlenghtstr(binarystring(text))
