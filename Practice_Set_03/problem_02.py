#Write a program to fill in a letter template given below with the name and date 

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Vivek").replace("<|Date|>","4 march 2030"))
