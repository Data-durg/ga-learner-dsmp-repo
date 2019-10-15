# --------------
# Importing header files
import numpy as np

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

#Loading data file and saving it into a new numpy array 
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print(data.shape)

#Concatenating the new record to the existing numpy array
census=np.concatenate((data, new_record),axis = 0)

print(census.shape)

#Code ends here


# --------------
#Code starts here
#Code starts here

#Subsetting the array to include only 'Age' column
age=census[:,0]
#Finding the max value of age
max_age=age.max()
print("Max Age= ",max_age)
print(age)
#Find the min value of age
min_age=age.min()
print("Min Age= ",min_age)

#Find the mean of age
age_mean=age.mean()
print("Age Average= ", age_mean)
#Find the standard deviation of age
age_std=age.std()
print("Age Standard Deviation= ",age_std)


#Code ends here


# --------------
#Code starts here
import numpy as np
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
minority_race=np.array([len_0,len_1,len_2,len_3,len_4]).argmin()
print(minority_race)
if len_0==minority_race:
    print('Race_0 is minority and its population is {0}'.format(minority_race))
elif len_1==minority_race:
    print('race_1 is minority and its population is {0}'.format(minority_race))
elif len_2==minority_race:
    print('Race_2 is minority and its population is {0}'.format(minority_race))
elif len_3==minority_race:
    print('Race_3 is minority and its population is {0}'.format(minority_race))
else:
    print('Race_4 is minority and its population is {0}'.format(minority_race))



# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens[:,6].sum()
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
if avg_pay_high>avg_pay_low:
    print('better education leads to better pay')
else:
    print('better education doesnot lead to better pay')


