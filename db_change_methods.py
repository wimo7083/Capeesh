
from app import db, models
from sqlalchemy import func
from app.models import *
from level_dict import l_dict as ld
import random

def word_table(level):
    switch_dict = {2:models.two, 3:models.three, 4:models.four, 5:models.five, 6:models.six, 7:models.seven, 8:models.eight, 9:models.nine}
    return switch_dict[level]

# returns 1 if user has been successfully input, 0 if there is another issue (duplicate username)
def new_user(input_name, curr_level):
    if verify_unique_name(input_name) is None:
        if db.session.query(func.max(User.UID)).scalar() is None:
            max = 1
        else:
            max =  1 + db.session.query(func.max(User.UID)).scalar()# find the maximum UID, add one to get the next id.
        db.session.add(models.User(UID= max, name = input_name ,current_level =  curr_level, initial_level = curr_level, first_success = None))
        db.session.commit()
        return 1
    
    else:
        return 0
    
def change_level(user_id, new_level, bool_success):
    user = User.query.filter_by(UID= user_id).first()
    if not user.first_success and bool_success:
        user.first_success = user.current_level
    user.current_level = new_level
    return user.current_level
        
        
def get_attempts(user_id, curr_level):
    user = Level_attempt.query.filter_by(UID = user_id).first()
    return user.ld[curr_level]
    
    
def modify_attempts(user_id, curr_level, attempts):
    user = Level_attempt.query.filter_by(UID = user_id).first()
    user.ld[curr_level] = attempts
    
def get_mistakes(user_id, queried_level):
    user = Level_mistakes.query.filter_by(UID = user_id).first()
    return user.ld[queried_level]
  
def modify_mistakes(user_id, curr_level, mistakes):
    user = Level_mistakes.query.filter_by(UID = user_id).first()
    user.ld[queried_level]= mistakes
    

def pick_words(curr_level):
    table_using = word_table(curr_level)    
    total_words = db.session.query(func.count(table_using.word)).scalar()
    word_lists = random.sample(range(total_words),5)      
    randomized_words = [db.session.query(table_using)[i].word for i in word_lists]
    return randomized_words

def verify_unique_name(desired_name):
    return User.query.filter_by(name = desired_name).first()
       

  
def initialize_word_list(word_level, word_value):     
    
    db.session.add(word_table(word_table)(level = word_level, word = word_value))
    db.session.commit()
   
#initialize_word_list(3, 'chissshit')
def query_all_words():    
    for i in range(2,10):
        words = word_table(i).query.all()
        for u in words:
            print(u.word)
            
            
#words = models.Words.query.all()
#for u in words:


 #   print(u.word)
    
print(new_user('Jesus', 3))
#make a new user
users = models.User.query.all()
print(users)
# view all users. 
