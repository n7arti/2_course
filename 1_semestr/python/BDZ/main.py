import pandas as pd

data = pd.read_csv('train.csv')
print(data)

# TASK1
print("\nTASK 1")
print(data.groupby(['Sex', 'Pclass'])[['Survived']].aggregate('mean').unstack())

# TASK2
print("\nTASK 2")
print(data.groupby('Sex')[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare']].mean())

# TASK3
print("\nTASK 3")
print(data.groupby('Embarked')[['Survived']].mean())

# TASK4
print("\nTASK 4")
Name1 = []
for i in data.Name:
    if '(' in i:
        Name1.append(i.split('(')[1].split(' ')[0].split(')')[0])
    else:
        Name1.append(i.split('. ')[1].split(' ')[0])
print(pd.DataFrame.from_dict(Name1)[0].value_counts()[:10])

# TASK5
print("\nTASK 5")
print(data.isnull().sum())
data.Embarked.fillna(data.Embarked.mode()[0], inplace=True)
data.Cabin = data.Cabin.fillna('Z')
data['Appeal'] = data.Name.apply(lambda name: name.split(',')[1].split('.')[0].strip())
group = data.groupby(['Sex', 'Pclass'])
group.Age.apply(lambda x: x.fillna(x.median()))
data.Age.fillna(data.Age.median, inplace=True)

# TASK6
print("\nTASK 6")
test = pd.read_csv('test.csv')
print(test)
print(test.isnull().sum())
test.Cabin = test.Cabin.fillna('Z')
test['Appeal'] = data.Name.apply(lambda name: name.split(',')[1].split('.')[0].strip())
group1 = test.groupby(['Sex', 'Pclass'])
group1.Age.apply(lambda x: x.fillna(x.median()))
test.Age.fillna(test.Age.median, inplace=True)
test.Fare.fillna(test.Fare.mean(), inplace=True)

print(data.groupby(['Sex'])[['Survived']].aggregate('mean').unstack())
print(data.groupby(['Pclass'])[['Survived']].aggregate('mean').unstack())
print(data.groupby(['SibSp'])[['Survived']].aggregate('mean').unstack())
print(data.groupby(['Parch'])[['Survived']].aggregate('mean').unstack())
data['SRFare'] = data.Fare.apply(lambda numb: numb // 100)
print(data.groupby(['SRFare'])[['Survived']].aggregate('mean').unstack())
data['NumbCabin'] = data.Cabin.apply(lambda numb: numb[0])
print(data.groupby(['NumbCabin'])[['Survived']].aggregate('mean').unstack())
print(data.groupby(['Embarked'])[['Survived']].aggregate('mean').unstack())

female = 0.742038
male = 0.188908

class1 = 0.629630
class2 = 0.472826
class3 = 0.242363

SibSp0 = 0.345395
SibSp1 = 0.535885
SibSp2 = 0.464286
SibSp3 = 0.250000
SibSp4 = 0.166667
SibSp5 = 0.000000
SibSp8 = 0.000000

Parch0 = 0.343658
Parch1 = 0.550847
Parch2 = 0.500000
Parch3 = 0.600000
Parch4 = 0.000000
Parch5 = 0.200000
Parch6 = 0.000000

SRFare0 = 0.361575
SRFare1 = 0.757576
SRFare2 = 0.647059
SRFare5 = 1.000000

CabinA = 0.466667
CabinB = 0.744681
CabinC = 0.593220
CabinD = 0.757576
CabinE = 0.750000
CabinF = 0.615385
CabinG = 0.500000
CabinT = 0.000000
CabinZ = 0.299854

EmbarkedC = 0.553571
EmbarkedQ = 0.389610
EmbarkedS = 0.339009

test['Survived'] = test.Sex.apply(lambda numb: female if numb == "female" else male)
test.Survived = test.Pclass.apply(lambda numb: +class1 if numb == 1 else (+class2 if numb == 2 else +class3))
print(test.Survived)
