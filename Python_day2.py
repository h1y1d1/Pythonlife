Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(double quotes pettala?)
SyntaxError: invalid syntax
>>> print("double quotes pettala?")
double quotes pettala?
>>> print('double quotes pettala?')
double quotes pettala?
>>> print('don't use single quotes')
      
SyntaxError: invalid syntax
>>> print("don't use single quotes")
don't use single quotes
>>> print("surya is good boy")
surya is good boy
>>> print("surya isnt good boy")
surya isnt good boy
>>> story = """thandaneee thaneee thane thandaneeee."""
>>> story = """thandaneee thaneee thane thandaneeee. hcgfeusefcboewuibcvewiubvciewlbfcewvbfciwfevfcfveuffcevbcvecvbshcvfu ecjhesbcj dgbcjehgb cbehj eebcbiusuvs hdiuusedb dciuesbuie wtgryyudjcc eguyeywqwowpos ehuiduwedu euhdideuh """
>>> print(story)
thandaneee thaneee thane thandaneeee. hcgfeusefcboewuibcvewiubvciewlbfcewvbfciwfevfcfveuffcevbcvecvbshcvfu ecjhesbcj dgbcjehgb cbehj eebcbiusuvs hdiuusedb dciuesbuie wtgryyudjcc eguyeywqwowpos ehuiduwedu euhdideuh 
>>> thandaneee thaneee thane thandaneeee. hcgfeusefcboewuibcvewiubvciewlbfcewvbfciwfevfcfveuffcevbcvecvbshcvfu ecjhesbcj dgbcjehgb cbehj eebcbiusuvs hdiuusedb dciuesbuie wtgryyudjcc eguyeywqwowpos ehuiduwedu euhdideuh
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> story="surya chandana"
>>> print(story)
surya chandana
>>> maths marks = 65
SyntaxError: invalid syntax
>>> maths_marks = 65
>>> print(maths_marks)
65
>>> print(maths_marks) # This is my math marks
65
>>> eng_marks = 47
>>> print(maths_marks,eng_marks)
65 47
>>> print(maths_marks,eng_marks,sep="e")
65e47
>>> print(maths_marks,eng_marks,sep="   ")
65   47
>>> print(maths_marks,eng_marks,sep="   ", end="/")
65   47/
>>> print(maths_marks,eng_marks,sep="   ", end="/n")
65   47/n
>>> print(maths_marks,eng_marks,sep="   ", end="\n")
65   47
>>> print("my math marks are",maths_marks,"my english marks are",eng_marks)
my math marks are 65 my english marks are 47
>>> print("my math marks are","maths_marks","my english marks are",eng_marks)
my math marks are maths_marks my english marks are 47
>>> print("my math marks are",maths_marks,"my english marks are",eng_marks)
my math marks are 65 my english marks are 47
>>> print(maths_marks,eng_marks,sep=" \n")
65 
47
>>> print(maths_marks) this is my math marks
SyntaxError: invalid syntax
>>> print(maths_marks) #this is my math marks
65
>>> print("my maths marks",math_marks, "my englishh marks",english marks,sep="\n')
      
SyntaxError: invalid syntax
>>> print("my maths marks",math_marks, "my englishh marks",english_marks,sep="\n')
      
SyntaxError: EOL while scanning string literal
>>> print("my maths marks",math_marks, "my englishh marks",english_marks,sep="\n")
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print("my maths marks",math_marks, "my englishh marks",english_marks,sep="\n")
NameError: name 'math_marks' is not defined
>>> print("my maths marks",maths_marks, "my englishh marks",english_marks,sep="\n")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print("my maths marks",maths_marks, "my englishh marks",english_marks,sep="\n")
NameError: name 'english_marks' is not defined
>>> print("my maths marks",maths_marks, "my english marks",eng_marks,sep="\n")
my maths marks
65
my english marks
47
>>> print("surya44")
surya44
>>> print("44")
44
>>> print(44)
44
>>> num = 44
>>> not_num = "44"
>>> print(num)
44
>>> print(type(num))
<class 'int'>
>>> print(type(not_num))
<class 'str'>
>>> 