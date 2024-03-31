# %% [markdown]
# # US Medical Insurance Costs Project
# 
# ### Introduction and data structure
# 
# This project works to analyze trends in the US Medical Insurance Costs dataset. We will primarily investigate the effects of each variable on the cost of medical insurance.
# 
# The data contains 1338 observations on 7 variables: `age`, `sex`, `bmi`, `children`, `smoker`, `region`, and `charges`. Specifically:
# - `age`, an integer variable, refers to the age of the patient in years.
# - `sex`, a string variable, refers to the biological sex of the patient (male or female.)
# - `bmi`, a float variable, refers to the Body Mass Index (BMI) of the patient, a common indicator of health.
# - `children`, an integer variable, refers to the number of children the patient has.
# - `smoker`, a string variable, refers to if the patient smokes or not (yes or no.)
# - `region`, a string variable, refers to the region the patient lives in (southwest, southeast, northwest, or northeast.)
# - `charges`, a float variable, refers to the cost of medical insurance, in dollars, for the patient.
# 
# ### Data integration
# 
# We will start by importing the data by reading in the `insurance.csv` file as lists.

# %%
# import libraries
import csv
import statistics

#Create empty lists for the various attributes in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])
        # return the list
        return lst
    
# look at the data in insurance_csv_dict
load_list_data(ages, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'age')
load_list_data(sexes, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'sex')
load_list_data(bmis, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'bmi')
load_list_data(num_children, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'children')
load_list_data(smoker_statuses, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'smoker')
load_list_data(regions, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'region')
load_list_data(insurance_charges, "C:/Users/nicol/Downloads/python-portfolio-example-solution/python-portfolio-example-solution/insurance.csv", 'charges')



# %% [markdown]
# ### Exploratory data analysis
# 
# First, we will explore some overall trends of the data set by calculating some summary statistics of the costs in the data set.

# %%
## average
insurance_charges = [float(x) for x in insurance_charges] #convert charges list from string to float
mean_costs = round(sum(insurance_charges) / len(insurance_charges), 2) #calculate mean
print("The average cost for patients in the dataset is", mean_costs, "dollars.")

## standard deviation
std_dev_costs = round(statistics.stdev(insurance_charges),2)
print("The standard deviation of the patient's costs is", std_dev_costs, "dollars.")

## minimum and maximum value
min_cost = min(insurance_charges)
max_cost = max(insurance_charges)
print("The cheapest cost in the dataset is", min_cost, "dollars, and the most expensive cost in the data set is", max_cost, "dollars.")

# %% [markdown]
# Now, we will explore each of the variables individually and their relationship with the cost variable.

# %% [markdown]
# #### Age
# 
# First, we will calculate some summary statistics of the ages of the patients in the dataset in order to gain a better picture of the data set.

# %%
## average age
ages = [int(x) for x in ages] #convert ages list from string to integers
mean_age = round(sum(ages) / len(ages), 2) #calculate mean
print("The average age of the patients in the dataset is", mean_age, "years.")

## standard deviation
std_dev_age = round(statistics.stdev(ages),2)
print("The standard deviation of the patient's ages is", std_dev_age, "years.")

## minimum and maximum value
min_age = min(ages)
max_age = max(ages)
print("The youngest patient in the dataset is", min_age, "years old, and the oldest patient in the data set is", max_age, "years old.")

# %% [markdown]
# From the above analysis, we can see that the ages of the patients in the dataset are pretty widely distributed.
# 
# There may be a correlation between the age range of the patient and the average medical insurance cost. We will separate the patients into age categories and calculate the average cost for each age range. For our age ranges, we will use a standard age range distribution as follows:
# - 18 to 24
# - 25 to 34
# - 35 to 44
# - 45 to 54
# - 55 to 64

# %%
## average cost by age range

# iterate through each age, categorize by age range, calculate mean cost 
tot_18 = 0
tot_25 = 0
tot_35 = 0
tot_45 = 0
tot_55 = 0

num_18 = 0
num_25 = 0
num_35 = 0
num_45 = 0
num_55 = 0

i = -1

for age in ages:
    i += 1
    cost = insurance_charges[i]
    if age < 25:
        tot_18 += cost
        num_18 += 1
    elif age < 35:
        tot_25 += cost
        num_25 += 1
    elif age < 45:
        tot_35 += cost
        num_35 += 1
    elif age < 55:
        tot_45 += cost
        num_45 += 1
    elif age < 65:
        tot_55 += cost
        num_55 += 1

# calculate mean, unless there are no observations in that age range
if num_18 != 0:
    avg_18 = round(tot_18 / num_18 , 2)
else:
    avg_18 = 0
if num_25 != 0:
    avg_25 = round(tot_25 / num_25 , 2)
else:
    avg_25 = 0
if num_35 != 0:
    avg_35 = round(tot_35 / num_35 , 2)
else:
    avg_35 = 0
if num_45 != 0:
    avg_45 = round(tot_45 / num_45 , 2)
else:
    avg_45 = 0
if num_55 != 0:
    avg_55 = round(tot_55 / num_55 , 2)
else:
    avg_55 = 0

print("The average cost for the", "18 to 24", "age range is", avg_18, "dollars, with", num_18, "total observations.")
print("The average cost for the", "25 to 34", "age range is", avg_25, "dollars, with", num_25, "total observations.")
print("The average cost for the", "35 to 44", "age range is", avg_35, "dollars, with", num_35, "total observations.")
print("The average cost for the", "45 to 54", "age range is", avg_45, "dollars, with", num_45, "total observations.")
print("The average cost for the", "55 to 64", "age range is", avg_55, "dollars, with", num_55, "total observations.")



# %% [markdown]
# From the above analysis, we can see that insurance cost seems to increase with age. We can also see that the sample size in each of the age ranges is approximately equal. To further investigate this correlation, we could run an ANOVA test for difference in group means or use regression analysis to find the correlation of the two variables. 
# 
# #### Sex
# 
# First, we will look at the distribution of the sexes of the patients in the dataset in order to gain a better picture of the data set.

# %%
## number of ppl in each sex

num_f = 0
num_m = 0

for sex in sexes:
    if sex == "female":
        num_f += 1
    if sex == "male":
        num_m += 1

print("There are", num_f, "females and", num_m, "males in the dataset.")

# %% [markdown]
# The number of females and males in the dataset is approximately equal. We can now look at the difference in costs between the sexes.

# %%
## average cost by sex

tot_f = 0
tot_m = 0

i = -1

for sex in sexes:
    i += 1
    cost = insurance_charges[i]
    if sex == "female":
        tot_f += cost
    if sex == "male":
        tot_m += cost

avg_f = round(tot_f / num_f, 2)
avg_m = round(tot_m / num_m, 2)

print("The average cost for females is", avg_f, "dollars.")
print("The average cost for males is", avg_m, "dollars.")


# %% [markdown]
# It seems that the average cost of medical insurance for males is higher than the average cost of medical insurance for females. To further investigate this difference, we could run an ANOVA test for the difference between means.
# 
# #### BMI
# 
# First, summary statistics. 

# %%
## average bmi
bmis = [float(x) for x in bmis] #convert bmi list from string to float
mean_bmi = round(sum(bmis) / len(bmis), 2) #calculate mean
print("The average BMI of the patients in the dataset is", mean_bmi)

## standard deviation
std_dev_bmi = round(statistics.stdev(bmis),2)
print("The standard deviation of the patient's BMI is", std_dev_bmi)

## minimum and maximum value
min_bmi = min(bmis)
max_bmi = max(bmis)
print("The smallest BMI in the dataset is", min_bmi, "and the largest in the data set is", max_bmi)

# %% [markdown]
# From the above analysis, we can see that there is a large spread of BMIs in the data set. Unfortunately, it seems that on average, the patients BMI indicates that they are obese (over 30.) America!
# 
# Now, we will investigate the difference in mean costs between the different BMI ranges. The BMI ranges we will use will be as follows:
# 
# - Underweight: 18.5 or below
# - Healthy weight: 18.5-25 (non-inclusive)
# - Overweight: 25(inclusive)-30(non-inclusive)
# - Obese: 30 or above

# %%
## insurance cost by bmi range

# iterate through bmi list, categorize by range, calculate mean of each range

# init vars
tot_uw = 0
tot_hw = 0
tot_ow = 0
tot_ob = 0

num_uw = 0
num_hw = 0
num_ow = 0
num_ob = 0

i = -1

# iteration (categorization)
for bmi in bmis:
    i += 1
    cost = insurance_charges[i]
    if bmi <= 18.5:
        tot_uw += cost
        num_uw += 1
    elif bmi < 25:
        tot_hw += cost
        num_hw += 1
    elif bmi < 30:
        tot_ow += cost
        num_ow += 1
    elif bmi >= 30:
        tot_ob += cost
        num_ob += 1


# calculate means
avg_uw = round(tot_uw / num_uw, 2)
avg_hw = round(tot_hw / num_hw, 2)
avg_ow = round(tot_ow / num_ow, 2)
avg_ob = round(tot_ob / num_ob, 2)

print("The average medical insurance cost for underweight patients is", avg_uw, "dollars, with", num_uw, "observations.")
print("The average medical insurance cost for healthy weight patients is", avg_hw, "dollars, with", num_hw, "observations.")
print("The average medical insurance cost for overweight patients is", avg_ow, "dollars, with", num_ow, "observations.")
print("The average medical insurance cost for obese patients is", avg_ob, "dollars, with", num_ob, "observations.")


# %% [markdown]
# It seems that the average medical insurance cost increases with BMI, but it should be noted that there is a large difference in sample size for each of the groups. The obese patients group makes up over half the data set. Because of the large disparity in sample sizes, it may be worthwhile to categorize based on a different scale. 
# 
# For further analysis, we can test for correlation between increase in BMI and increase in medical insurance cost using regression analysis. In this case, we won't have to deal with the differing sample sizes.
# 
# #### Children
# 
# First, summary statistics.

# %%
## average children
num_children = [int(x) for x in num_children] #convert bmi list from string to float
mean_children = round(sum(num_children) / len(num_children), 2) #calculate mean
print("The average number of children of the patients in the dataset is", mean_children, "children.")

## standard deviation
std_dev_children = round(statistics.stdev(num_children),2)
print("The standard deviation of the patient's number of children is", std_dev_children, "children.")

## minimum and maximum value
min_children = min(num_children)
max_children = max(num_children)
print("The smallest number of children in the dataset is", min_children, "children and the largest number of children in the data set is", max_children, "children.")

# %% [markdown]
# Since the smallest number of children in the data set is 0, and the largest number is 5, we will categorize based on these integer values and calculate the group means.

# %%
tot_0c = 0
tot_1c = 0
tot_2c = 0
tot_3c = 0
tot_4c = 0
tot_5c = 0

num_0c = 0
num_1c = 0
num_2c = 0
num_3c = 0
num_4c = 0
num_5c = 0

i = -1

for num in num_children:
    i += 1
    cost = insurance_charges[i]
    if num == 0:
        tot_0c += cost
        num_0c += 1
    if num == 1:
        tot_1c += cost
        num_1c += 1
    if num == 2:
        tot_2c += cost
        num_2c += 1
    if num == 3:
        tot_3c += cost
        num_3c += 1
    if num == 4:
        tot_4c += cost
        num_4c += 1
    if num == 5:
        tot_5c += cost
        num_5c += 1

avg_0c = round(tot_0c / num_0c, 2)
avg_1c = round(tot_1c / num_1c, 2)
avg_2c = round(tot_2c / num_2c, 2)
avg_3c = round(tot_3c / num_3c, 2)
avg_4c = round(tot_4c / num_4c, 2)
avg_5c = round(tot_5c / num_5c, 2)

print("The average insurance cost for patients with 0 children is", avg_0c, "dollars, with", num_0c, "observations.")
print("The average insurance cost for patients with 1 child is", avg_1c, "dollars, with", num_1c, "observations.")
print("The average insurance cost for patients with 2 children is", avg_2c, "dollars, with", num_2c, "observations.")
print("The average insurance cost for patients with 3 children is", avg_3c, "dollars, with", num_3c, "observations.")
print("The average insurance cost for patients with 4 children is", avg_4c, "dollars, with", num_4c, "observations.")
print("The average insurance cost for patients with 5 children is", avg_5c, "dollars, with", num_5c, "observations.")

# %% [markdown]
# It seems like the relationship between number of children and insurance cost is non linear, with the highest insurance costs being in the group with 2 and 3 children and lower insurance costs with 0, 1, 4, or 5 children. Further analysis is needed to investigate this relationship. In addition, it should be noted that there are significantly less observations for patients with 4 and 5 children, and significantly more observations for patients with 0 children.
# 
# #### Smoking status
# 
# First, summary statistics.

# %%
## number of ppl in each smoking status

num_y = 0
num_n = 0

for patient in smoker_statuses:
    if patient == "yes":
        num_y += 1
    if patient == "no":
        num_n += 1

print("There are", num_y, "smokers and", num_n, "non-smokers in the dataset.")

# %% [markdown]
# The number of smokers and non-smokers in the dataset is unequal. However, we will still calculate the group means of each group.

# %%
tot_y = 0
tot_n = 0

i = -1

for patient in smoker_statuses:
    i += 1
    cost = insurance_charges[i]
    if patient == "yes":
        tot_y += cost
    if patient == "no":
        tot_n += cost

avg_y = round(tot_y / num_y, 2)
avg_n = round(tot_n / num_n, 2)

print("The average insurance cost for smokers is", avg_y, "dollars, and", avg_n, "dollars for non-smokers.")

# %% [markdown]
# It seems like the average insurance cost is less for non-smokers. Further analysis is needed, we could run an ANOVA test for the difference between means.
# 
# #### Region
# 
# First, summary statistics.

# %%
## number of ppl in each smoking status

num_sw = 0
num_se = 0
num_nw = 0
num_ne = 0

for region in regions:
    if region == "southwest":
        num_sw += 1
    if region == "southeast":
        num_se += 1
    if region == "northwest":
        num_nw += 1
    if region == "northeast":
        num_ne += 1

print("There are", num_sw, "patients from the Southwest,", num_se, "patients in the Southeast,", num_nw, "patients in the Northwest, and", num_ne, "patients in the Northeast.")

# %% [markdown]
# It seems like the number of patients from each region is approximately equal. We will now calculate the group means of each region.

# %%
## number of ppl in each smoking status

tot_sw = 0
tot_se = 0
tot_nw = 0
tot_ne = 0

i = -1

for region in regions:
    i += 1
    cost = insurance_charges[i]
    if region == "southwest":
        tot_sw += cost
    if region == "southeast":
        tot_se += cost
    if region == "northwest":
        tot_nw += cost
    if region == "northeast":
        tot_ne += cost

avg_sw = round(tot_sw / num_sw, 2)
avg_se = round(tot_se / num_se, 2)
avg_nw = round(tot_nw / num_nw, 2)
avg_ne = round(tot_ne / num_ne, 2)

print("The average insurance cost for patients in the Southwest is", avg_sw, "dollars.")
print("The average insurance cost for patients in the Southeast is", avg_se, "dollars.")
print("The average insurance cost for patients in the Northwest is", avg_nw, "dollars.")
print("The average insurance cost for patients in the Northeast is", avg_ne, "dollars.")



# %% [markdown]
# It seems like the insurance cost for patients in the east is slightly higher than those in the west. Further analysis is needed; we could run an ANOVA test for difference between group means.
# 
# ### Conclusion
# 
# Overall, there are many interesting trends to be found in the medical insurance data set. Further analysis can be done through statistical testing such as ANOVA or regression analysis. 


