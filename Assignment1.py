#import all required packages here
import math
#import numpy as np
from sklearn.metrics import confusion_matrix

#Question 1

# list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list and find the min and max age
ages_s = sorted(ages)
min_age = min(ages_s)
max_age = max(ages_s)
print("Ages list has minimum age of {} and maximum age of {}".format(min_age, max_age))

#Add the min age and the max age again to the list
ages_new = [min_age] + ages_s + [ max_age]
print("New ages list after adding min and max age again is ", ages_new)

#Find the median age (since length is even its two middle items divided by two)
l = len(ages_new)
median = (ages_new[(l//2)-1]+ages_new[(l//2)])/2
print("Median age of given ages list is ", median)

#Find the average age (sum of all items divided by their number)
sm = 0
for i in range(0,l):
    sm = sm+ages_new[i]
average = sm/l
print("Average age of given ages list is ", average)

#Find the range of the ages (max minus min)
rng = ages_new[-1] - ages_new[0]
print("Range of the ages is ",rng)

print("*"*20)

#Question 2

#Create an empty dictionary called dog
dog = {}

#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "prisky"
dog['color'] = "caramel brown"
dog['breed'] = "teddy bear"
dog['legs'] = 4
dog['age'] = 2
print("Dog dictionary is ", dog)

#Create a student dictionary and add first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary
student = {'first_name':"Kavyasri", 'last_name':"Avushapuram", 'gender':"Female", 'age':27, 'marital_status':"Married",
           'skills':["Programming", "Painting", "Dancing"], 'country':"USA", 'city':"Kansas city", 'address':"140 floyd street, sandstone creek, Overlandpark, 66223"}
print("Initial student dictionary is ", student)

#Get the length of the student dictionary
print("Length of student dictionary is ",len(student))

#Get the value of skills and check the data type, it should be a list
print("Type of student skills is ", type(student['skills']))

#Modify the skills values by adding one or two skills
student['skills'] = student['skills']+["Cooking", "Gaming"]
print("New student skills are ", student['skills'])

#Get the dictionary keys as a list
student_keys = list(student.keys())
print("Student dictionary keys are ", student_keys)

#Get the dictionary values as a list
student_values = list(student.values())
print("Student dictionary values are ", student_values)

print("*"*20)

#Question 3

#Create a tuple containing names of your sisters and your brothers
sisters = ("Amaya", "Ritu", "Tanya")
brothers = ("Rohan", "Samay", "Vicky")

#Join brothers and sisters tuples and assign it to siblings
siblings =  sisters+brothers
print("Siblings names are ", siblings)

#How many siblings do you have?
print("Number of siblings are ",len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings+("Raghava", "Meghana")
print("Family members are ", family_members)

print("*"*20)

#Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print("Length of the set it_companies", len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("IT companies after adding Twitter are", it_companies)

#Insert multiple IT companies at once to the set it_companies
new_it_companies = it_companies.union({'Cognizant', 'Wipro', 'Fidelity'})
print("IT companies after adding 3 more are", new_it_companies)

#Remove one of the companies from the set it_companies
new_it_companies.discard('Cognizant')
print("IT companies after removing Cognizant are", new_it_companies)

#What is the difference between remove and discard
"""discard() removes a specified entry. 
   remove() functions similarly except that t throws error when an entry is not found."""

#Join A and B
joined = A.union(B)
print("Joining A and B gives ", joined)

#Find A intersection B
print("A intersection B gives ",A.intersection(B))

#Is A subset of B (checking if B is superset instead
print("Is A subset of B: ", B.issuperset(A))

#Are A and B disjoint sets
print("A and B disjoint sets: ",A.isdisjoint(B))

#Join A with B and B with A
B.update(A)
A.update(B)
print("Updated A", A)
print("Updated B", B)

#What is the symmetric difference between A and B
print("Symmetric difference between A and B is ", A.symmetric_difference(B))

#Delete the sets completely
del A
del B

#Convert the ages to a set and compare the length of the list and the set.
age_set = set(age)
print("Length of age list is {} and age set is {}".format(len(age),len(age_set)))

#Question 5

#The radius of a circle is 30 meters
rad = 30
_area_of_circle_ = math.pi*rad*rad
_circum_of_circle_ = 2*math.pi*rad
print("Area of circle with radius 30 meters is {} square meters".format(_area_of_circle_))
print("Circumference of circle with radis 30 meters is {} meters".format(_circum_of_circle_))

#Take radius as user input and calculate the area
inp_rad = float(input("Enter a radius value: "))
area = math.pi*inp_rad*inp_rad
print("Area of circle with radius {} meters is {} square meters".format(inp_rad,area))

print("*"*20)

#Question 6

""" 'I am a teacher and I love to inspire and teach people'
• How many unique words have been used in the sentence? Use the split methods and set
to get the unique words."""

sentence = "I am a teacher and I love to inspire and teach people"
sent_list = sentence.split(" ")
sent_set = set(sent_list)
print("Number of unique words in 'I am a teacher and I love to inspire and teach people' is ", len(sent_set))

print("*"*20)

#Question 7
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

print("*"*20)

#Question 8

"""Use the string formatting method to display the following: """

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))

print("*"*20)

#Question 9
"""Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop. N: No of students (Read input from user)"""

wt = input("Enter the list of weights in lbs space seperated:")
wt_lst = wt.split()
wt_lst = [float(item) for item in wt_lst]
print("Weight list in lbs is ", wt_lst)
wt_kgs = [item*0.453592 for item in wt_lst]
print("Weight list in kgs is ", wt_kgs)

print("*"*20)

#Question 10
'''The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature
value, labeled f. Note that there are two data points with the same feature value of 6. These are
shown as two x’s one above the other.'''

#Divide this data equally into two parts. Use first part as training and second part as
#testing. Using KNN classifier, for K=3, what would be the predicted outputs for the test
#samples? Show how you arrived at your answer.

data_x = [1,2,3,6,6,7,10,11]
data_y = ["Yes","Yes","No","No","No","Yes","Yes","Yes"]
train_x = [2,3,6,7]
train_y = ["Yes","No","No","Yes"]
test_x = [1,6,10,11]
test_y = ["Yes","No","Yes","Yes"]

#Euclidean difference becomes simple difference since we have only one feature
def euclidean_distance_custom(val1, val2):
    return abs(val1-val2)

# Locate neighbors based on distance
def get_neighbors(train_values, train_labels, test_sample, num_neighbors=3):
    distances = list()
    for train_val,train_lab in zip(train_values,train_labels):
        dist = euclidean_distance_custom(test_sample, train_val)
        distances.append((train_lab, dist))
    #sorting list of tuples based on second key which is distance
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

outcome_all = []
for i,j in zip(test_x,test_y):
    out = get_neighbors(train_x, train_y, i)
    print("Expected outcome for point {} is {} and real label is {}".format(i,max(out,key=out.count),j))
    outcome_all.append(max(out,key=out.count))


#Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity values.
#Confusion matrix, Accuracy, sensitivity and specificity
cm = confusion_matrix(test_y,outcome_all)
print('Confusion Matrix : \n', cm)

total=sum(sum(cm))
#####from confusion matrix calculate accuracy
accuracy=(cm[0,0]+cm[1,1])/total
print ('Accuracy : ', accuracy)

sensitivity = cm[0,0]/(cm[0,0]+cm[0,1])
print('Sensitivity : ', sensitivity )

specificity = cm[1,1]/(cm[1,0]+cm[1,1])
print('Specificity : ', specificity)
