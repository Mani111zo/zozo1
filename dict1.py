import pandas as pd
screen_time = [2,4,6,8]
hours_sleeping = [10,12,13,16]
student_name = ["shisui,monet,sofie"]
dict1 = {
    
    "screen_time"= screen_time,
    "hours_sleeping"=hours_sleeping,
    "student_name"=student_name
}
print(dict1)
df = pd.DataFrame(dict1)
print(df)