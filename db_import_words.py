from app import db, models
from db_change_methods import initialize_word_list as iwl
import os
import csv
import sqlalchemy   

def import_words(filename):
        
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        words = list(reader)
        
    for row in words:
        level = int(row[0])
        print(level)
        for word in row[1:]:
            if word:
                iwl(level,word)      
        
    
    
    
    
if __name__ == "__main__":
    name = 'spelling_list.csv'
    #name = input('What is the filename you wish to import? ')
    file = os.path.dirname(os.path.realpath(__file__))+'\\'+name
    import_words(file)
    