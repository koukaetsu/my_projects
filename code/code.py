import base64
import string
import uu

class code(object):

    def __init__(self):
        pass

    def abccc(self):
        return '请输入正确的字符噢喵~'


class base644(code): #base64类

    def __init__(self, code_content):

        self.code_content = code_content

    def base64en(self): #base64编码

        raw_bytes = bytes(self.code_content, 'utf-8')
        e642 = base64.b64encode(raw_bytes)
        e64 = e642.decode()
        return e64

    def base64de(self): #base64解码

        #当输入的base64字符串不是3的倍数时添加相应的=号
        if(len(self.code_content)%3 == 1):
            self.code_content += "=="

        elif(len(self.code_content)%3 == 2):
            self.code_content += "="

        d64 = base64.b64decode(self.code_content)
        d642 = d64.decode()
        return d642


class hex1(code): #16进制类

    def __init__(self, code_content):

        self.code_content = code_content

    def hexen(self): #16进制编码

        by = bytes(self.code_content,'UTF-8')
        #print(by) #没办法的事，中文还是得转成utf-8形式，不过不影响就是了
        hen = by.hex()
        return hen

    def hexde(self): #16进制解码

        hde2 = base64.b16decode(self.code_content.upper())
        hde = hde2.decode()
        return hde


class Binary123(code): #2进制类

    def __init__(self, code_content):

        self.code_content = code_content

    def binaryen(self): #2进制编码
        cat = input('1.数字, 2.字符串')
        if cat == '1':
            binary_converted = format(int(self.code_content), 'b')
            return binary_converted

        #by = bytes(self.code_content,'UTF-8')
        elif cat == '2':
            binary_converted = ' '.join(format(ord(c), 'b') for c in self.code_content)
            return binary_converted

    def binaryde(self): #2进制解码(等等，2进制是编码？)
        try:
            str_converted = "".join(chr(int(s, 2)) for s in self.code_content.split())
            return str_converted
        except ValueError:
            return None

class UU(code): #uu类 用不了用不了！！只能用文件版本，未修复

    def __init__(self, code_content):
        self.code_content = code_content

    def uuen(self):
        uue = uu.encode(self.code_content)
        return uue

    def uude(self):
        uud = uu.decode(self.code_content)
        return uud

class morse(code): #摩斯电码类

    def __init__(self, code_content):

        self.code_content = code_content
        with open('letter_morse.txt', 'r', encoding='utf-8') as file:
             content = eval(file.read())
        self.letter_morse = content
        self.morse_letter = {v: k for k, v in self.letter_morse.items()}

    def morseen(self): #转摩斯电码

        for i2 in self.code_content: #将标点符号和空格去掉
            if i2 in string.whitespace:
                self.code_content = self.code_content.replace(i2,"")
            elif i2 in string.punctuation:
                self.code_content = self.code_content.replace(i2,"")
        ea = '/'.join(self.letter_morse.get(i.lower()) for i in self.code_content)
        return ea

    def morsede(self): #相反
        ae = ''.join(self.morse_letter.get(i) for i in self.code_content.split('/'))
        return ae

class Caesar(code): #凯撒密码类

    def __init__(self, code_content):

        self.code_content = code_content
        with open('letter.txt', 'r', encoding='utf-8') as file2:
             content2 = eval(file2.read())
        self.english_letter = content2
        for i in self.code_content: #将标点符号和空格去掉
            if i in string.whitespace:
                self.code_content = self.code_content.replace(i,"")
            elif i in string.punctuation:
                self.code_content = self.code_content.replace(i,"")

    def Caesaren(self):

        num = int(input('输入往前的位移值：'))
        conv_content = ''.join(self.english_letter[self.english_letter.index(i2.lower())-num] for i2 in self.code_content)
        return conv_content


    def Caesarde(self):
        num = int(input('输入往后的位移值：'))
        conv_content = ''.join(self.english_letter[self.english_letter.index(i2.lower())+num] for i2 in self.code_content)
        return conv_content


class run(object):

    def __init__(self, name):

        self.name = name


    def ende(self):

            choice = input("1.编码，2.解码")

            if choice == '1' and a1 == 'base64':
                base64_en = self.name.base64en()
                return base64_en

            elif choice == '2' and a1== 'base64':
                base64_de = self.name.base64de()
                return base64_de

            elif choice == '1' and a1 == 'hex':
                hex_en = self.name.hexen()
                return hex_en

            elif choice == '2' and a1 == 'hex':
                hex_de = self.name.hexde()
                return hex_de

            elif choice == '1' and a1 == '2':
                binary_en = self.name.binaryen()
                return binary_en

            elif choice == '2' and a1 == '2':
                binary_de = self.name.binaryde()
                return binary_de

            elif choice == '1' and a1 == 'morse':
                morse_en = self.name.morseen()
                return morse_en

            elif choice == '2' and a1 == 'morse':
                morse_de = self.name.morsede()
                return morse_de

            elif choice == '1' and a1 == 'caesar':
                caesar_en = self.name.Caesaren()
                return caesar_en

            elif choice == '2' and a1 == 'caesar':
                caesar_de = self.name.Caesarde()
                return caesar_de

            elif choice == '1' and a1 == 'uu':
                uu_en = self.name.uuen()
                return uu_en
            elif choice == '2' and a1 == 'uu':
                uu_de = self.name.uude()
                return uu_de
            else:
                abc = self.name.abccc()
                return abc


    def print_code(self):
        print(self.ende())


if __name__ == '__main__':

    c = input("输入编码或字符串")
    a1 = input("输入类型")

    if a1 == 'base64':
        a = base644(c)
    elif a1 == 'hex':
        a = hex1(c)
    elif a1 == '2':
        a = Binary123(c)
    elif a1 == 'morse':
        a = morse(c)
    elif a1 == 'caesar':
        a = Caesar(c)
    elif a1 == 'uu':
        a = UU(c)
    else:
        a = code()

    b = run(a)
    b.print_code()
