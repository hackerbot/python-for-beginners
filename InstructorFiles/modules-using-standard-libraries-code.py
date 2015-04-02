import datetime

start = datetime.datetime.now()


i =0 
while i < 10000:
    i = i + 1
    
end = datetime.datetime.now()

print(end - start)