import pandas

data = pandas.read_csv("Day 025/Exercises/Ex 01/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"]  == 'Gray'])
black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])

print(grey_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('Day 025/Exercises/Ex 01/squirrel_count.csv')
