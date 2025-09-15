"""
date_validate
"""
import datetime
date_list = [
    {'due_date': '10003-03-10'},
    {'due_date': '0003-03-10'},
    {'due_date': '12034-46-10'},
    {'due_date': '2024-01-01'}
]

due_date = ''
for date_text in date_list:
    try:
        date_obj = datetime.date.fromisoformat(date_text['due_date'])
        if date_obj.year < 1900:
            raise ValueError(f'{date_text["due_date"]} year < 1900')
        else:
            print(f'correct date: {date_text} {date_obj.year}')
            due_date = date_text['due_date']
            break
    except Exception as e:
        print({e})    

print(f'done due_date={due_date}')

from datetime import datetime
cur_date = datetime.now().date()
cur_date_str = cur_date.strftime("%Y-%m-%d")
print(f'cur_date={cur_date}, type={type(cur_date)} cur_date_str={cur_date_str}')