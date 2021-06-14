#BIBLIOTECA
from numpy import append
import pandas as pd
import datetime
import calendar
from collections import Counter
import seaborn as sns


#ARQUIVO
file = open('C:\MBA\Data Science Using Python\ProjetoWhatsApp\ProjetoWhatsAppSilasOliveiraRA2101625.txt', 'r', encoding='utf-8')
line = file.readline()

#ARRAYS
list_date = []
list_hour = []
list_weekday = []
list_person = []
list_message = []

#LER AQUIVO VALIDAR
while line:
    line = file.readline()
    
    try:
        date_obj = datetime.datetime.strptime(line[0:13], '%d/%m/%Y %H')
        
        list_date.append(date_obj)
        list_hour.append(date_obj.hour)

        if(date_obj.weekday() == 0):
            list_weekday.append('domingo')  
        elif(date_obj.weekday() == 1):
            list_weekday.append('segunda')
        elif(date_obj.weekday() == 2):
            list_weekday.append('terca')
        elif(date_obj.weekday() == 3):
            list_weekday.append('quarta')
        elif(date_obj.weekday() == 4):
            list_weekday.append('quinta')
        elif(date_obj.weekday() == 5):
            list_weekday.append('sexta')
        elif(date_obj.weekday() == 6):
            list_weekday.append('sabado')      

        msg = line[19:]
        
        if(len(msg.split(':')) >= 2):
            list_person.append(msg.split(':')[0])        
            if(msg[-1:-2:-1]) == '\n':
                newmsg = msg.strip()
                list_message.append(newmsg.split(':')[1])
            else:
                list_message.append(msg.split(':')[1])
   
    except ValueError:
        pass
file.close()

#FREQUENCIA CONVERSA POR PESSOA
dict_person = dict(Counter(list_person))
person_df = pd.DataFrame(dict_person.items(), columns=['Pessoa', 'Frequencia'])
person_df = person_df.sort_values(by=['Frequencia'], ascending=True)
person_df.plot(kind='bar', x='Pessoa', y='Frequencia', title='Frequencia de conversa por pessoa - Abril 2021')

#FRENQUENCIA CONVERSA POR HORA
dict_hour = dict(Counter(list_hour))
hour_df = pd.DataFrame(dict_hour.items(), columns=['Hora', 'Frequencia'])
hour_df = hour_df.sort_values(by=['Frequencia'], ascending=True)
hour_df.plot(kind='bar', x='Hora', y='Frequencia', title='Frequencia de conversa por hora do dia - Abril 2021')

#FREQUENCIA POR DIA SEMANA
dict_weekday = dict(Counter(list_weekday))      
week_df = pd.DataFrame(dict_weekday.items(), columns=['Dia da Semana', 'Frequencia'])
week_df = week_df.sort_values(by=['Frequencia'], ascending=True)
week_df.plot(kind='bar', x = 'Dia da Semana', y='Frequencia', title='Frequencia de conversa por dia da semana - Abril 2021')


#CONTAR PALAVRA
def word_count(msg):
    words = []
    for phrase in msg:
        for word in phrase.split():
            if word not in words_to_not_count and len(word) > 4 and 'kk' not in word and 'KK' not in word:
                words.append(word)
    return Counter(words)

#FREQUENACIA PALAVRA
words_dict = dict(word_count(list_message))
words_df = pd.DataFrame(words_dict.items(), columns=['Palavra', 'Frequencia'])
words_df = words_df.sort_values(by=['Frequencia'], ascending=False)
words_df.head(10).plot(kind='bar', x = 'Palavra', y='Frequencia', title='Frequencia de palavras nas conversas - Abril 2021')
