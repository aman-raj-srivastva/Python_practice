'''nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
  (a) What was the average temperature in first week of Jan
  (b) What was the maximum temperature in first 10 days of Jan
'''
arr=[]
with open('assets/nyc_weather.csv','r') as f:
    for line in f:
        token=line.split(',')
        try:
            temp=int(token[1])
            arr.append(temp)
        except:
            pass
print(arr)

avg_temp_first_week=sum(arr[:7])/7
print(avg_temp_first_week)

print(max(arr[:10]))

'''(a) What was the temperature on Jan 9?
   (b) What was the temperature on Jan 4?
'''
dict={}
with open('assets/nyc_weather.csv') as f:
    for line in f:
        token=line.split(',')
        day=token[0]
        try:
            temp=int(token[1])
            dict[day]=temp
        except:
            pass
print(dict)
print(dict['Jan 9'])
print(dict['Jan 4'])

word_count={}
with open('assets/poem.txt','r') as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            word=word.replace('\n','')
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
print(word_count)