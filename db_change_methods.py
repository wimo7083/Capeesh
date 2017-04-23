
from app import db, models
from sqlalchemy import func
from app.models import *
from level_dict import l_dict as ld

def new_user(input_name, curr_level):
    # find the maximum UID
    
    max =  1 + db.session.query(func.max(User.UID)).scalar()
    db.session.add(models.User(UID= max, name = input_name ,current_level =  curr_level,initial_level = curr_level, first_success = None))
    db.session.commit()
    
    
def change_level(user_id, new_level, bool_success):
    user = User.query.filter_by(UID= user_id).first()
    
    if user.first_success is not True and bool_success is True:
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
    
    
def initialize_word_list(word_level, word_value):     
    switch_dict = {2:models.two, 3:models.three, 4:models.four, 5:models.five, 6:models.six, 7:models.seven, 8:models.eight, 9:models.nine}

    db.session.add(switch_dict[word_level](level = word_level, word = word_value))
    db.session.commit()
   
#initialize_word_list(3, 'chissshit')
def query_all_words():
    switch_dict = {2:models.two, 3:models.three, 4:models.four, 5:models.five, 6:models.six, 7:models.seven, 8:models.eight, 9:models.nine}

    for i in range(2,10):
        words = switch_dict[i].query.all()
        for u in words:
            print(u.word)
#words = models.Words.query.all()
#for u in words:

query_all_words()
 #   print(u.word)
    
# new_user('Chester', 5)
#make a new user

# users = models.User.query.all()

# view all users. 
