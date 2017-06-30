
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from level_dict import l_dict as ld
import random

db = SQLAlchemy()

        



class User(db.Model):
    UID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index = True)
    current_level = db.Column(db.Integer, index = True)
    initial_level = db.Column(db.Integer, index = True)
    first_success = db.Column(db.Integer, index = True)     
    
    
    def __init__(self, name, curr_level):
    
        if verify_unique_name(input_name) is None:
            if db.session.query(func.max(User.UID)).scalar() is None:
                max = 1
            else:
                max =  1 + db.session.query(func.max(User.UID)).scalar()# find the maximum UID, add one to get the next id.
            self.UID = max
            self.name = name
            self.current_level = curr_level
            return 1
        else:
            return 0    
    
    def change_level(self, user_id, new_level, bool_success):
        user = User.query.filter_by(UID= user_id).first()
        if not user.first_success and bool_success:
            user.first_success = user.current_level
        user.current_level = new_level
        return user.current_level
        
    def verify_unique_name(desired_name):
        return User.query.filter_by(name = desired_name).first()
      
    
    def __repr__(self):
        return '<User %r>' % (self.name)
  
class Level_attempt(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    two = db.Column(db.Integer, index = True)     
    three = db.Column(db.Integer, index = True)
    four = db.Column(db.Integer, index = True)
    five = db.Column(db.Integer, index = True)
    six = db.Column(db.Integer, index = True)
    seven = db.Column(db.Integer, index = True)
    eight = db.Column(db.Integer, index = True)
    nine = db.Column(db.Integer, index = True) 
    
    def get_attempts(self, user_id, curr_level):
        user = Level_attempt.query.filter_by(UID = user_id).first()
        return user.ld[curr_level]
        
    
    def modify_attempts(self, user_id, curr_level, attempts):
        user = Level_attempt.query.filter_by(UID = user_id).first()
        user.ld[curr_level] = attempts


    
    def __repr__(self, level_num):    
        return '<Level_attempt %r>' % (self.level_num)
        
        
       
class Level_mistake(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    two = db.Column(db.Integer, index = True)     
    three = db.Column(db.Integer, index = True)
    four = db.Column(db.Integer, index = True)
    five = db.Column(db.Integer, index = True)
    six = db.Column(db.Integer, index = True)
    seven = db.Column(db.Integer, index = True)
    eight = db.Column(db.Integer, index = True)
    nine = db.Column(db.Integer, index = True)
    
    
    def get_mistakes(self, user_id, queried_level):
        user = Level_mistakes.query.filter_by(UID = user_id).first()
        return user.ld[queried_level]
      
    def modify_mistakes(self, user_id, curr_level, mistakes):
        user = Level_mistakes.query.filter_by(UID = user_id).first()
        user.ld[queried_level]= mistakes
    
    def __repr__(self, level_num):    
        return '<Level_attempt %r>' % (self.level_num)
        
        
     
    
class two(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
        
class three(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)

class four(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
class five(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
class six(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
class seven(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
class eight(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)
    def __repr__(self):
        return '<Word %r>' % (self.word)
        
        
class nine(db.Model):
    level = db.Column(db.Integer, unique=False, index= True)
    word = db.Column(db.String(32), primary_key = True)   
    def __repr__(self):
        return '<Word %r>' % (self.word)
   

def word_table(level):
    switch_dict = {2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine}
    return switch_dict[level]   
    

def pick_words(curr_level):
    table_using = word_table(curr_level)    
    total_words = db.session.query(func.count(table_using.word)).scalar()
    word_lists = random.sample(range(total_words),5)      
    randomized_words = [db.session.query(table_using)[i].word for i in word_lists]
    return randomized_words



def query_all_words():    
    for i in range(2,10):
        words = word_table(i).query.all()
        for u in words:
            print(u.word)
            
"""           
#words = models.Words.query.all()
#for u in words:


 #   print(u.word)
    
#print(new_user('Jesus', 3))
#make a new user
#users = models.User.query.all()
#print(users)
# view all users. 
"""
   