import random

#word list separated by type
articles = ["o","os","a","as","um","uns","uma","umas"]
subjects = ["Maya", "Cachorro", "Adriel", "Mabel", "Rapaz", "Moça", "Gato","Rato", "Rei de roma", "Gabriela","Pedro","Matheus"]
verbs = ["nascer","viver","proceder","cair","chorar","dormir","deitar"]
adverbs = ["Hoje","já","afinal","logo","agora","amanhã","amiúde","antes","ontem","tarde","breve","cedo","depois","enfim","ainda","jamais","nunca","sempre","doravante","outrora"]

#list containing the sentence construction by word type
sentence = [[articles,subjects,verbs,adverbs],[articles,subjects,verbs]]


#input the number of lines to be generated
while True:
    try:
        lines_number = int(input("Number of lines: "))
        break
    except ValueError as err:
        print("invalid value")
        continue


#sentence construction
lines = 0
while lines < lines_number:
    sentense_type = sentence[random.randint(0,1)]
    line = ""
    column = 0
    while column < len(sentense_type):
        line += random.choice(sentense_type[column])
        line += " "
        column += 1
    print(line)
    lines += 1