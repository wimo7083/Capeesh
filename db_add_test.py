
from app import db, models

u = models.User(UID= 6, name = 'Jonny2',current_level =  2,initial_level = 2, first_success = None)


y = models.User(UID= 7, name = 'Test2',current_level =  2,initial_level = 2, first_success = None)
"""
db.session.add(u)
db.session.add(y)
db.session.commit()
"""

print(users)


def new_user(input_name, curr_level):
    # find the maximum UID
    db.session.add(models.User(UID= 7, name = input_name ,current_level =  curr_level,initial_level = curr_level, first_success = None))
    db.session.commit()