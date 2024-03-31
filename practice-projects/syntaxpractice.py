# %% [markdown]
# # Python Syntax: Medical Insurance Project

# %% [markdown]
# Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. Using a formula that estimates a person's yearly insurance costs, you will investigate how different factors such as age, sex, BMI, etc. affect the prediction.

# %% [markdown]
# ## Setting up Factors

# %% [markdown]
# 1. Our first step is to create the variables for each factor we will consider when estimating medical insurance costs.
# 
#    These are the variables we will need to create:
#    - `age`: age of the individual in years
#    - `sex`: 0 for female, 1 for male*
#    - `bmi`: individual's body mass index
#    - `num_of_children`: number of children the individual has
#    - `smoker`: 0 for a non-smoker, 1 for a smoker
#    
#    In the code block below, create the following variables for a **28**-year-old, **nonsmoking woman** who has **three children** and a **BMI** of **26.2**.
#    
#    **Note**: We are using this [medical insurance dataset](https://www.kaggle.com/mirichoi0218/insurance) as a guide, which unfortunately does not include data for non-binary individuals.

# %%
# create the initial variables below

age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0


# %% [markdown]
# ## Working with the Formula

# %% [markdown]
# 2. After the declaration of the variables, create a variable called `insurance_cost` that utilizes the following formula:
# 
#    $$
#    \begin{aligned}
#    insurance\_cost = 250*age - 128*sex \\
#    + 370*bmi + 425*num\_of\_children \\
#    + 24000*smoker - 12500 \\
#    \end{aligned}
#    $$

# %%
# Add insurance estimate formula below
insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500

print(insurance_cost)


# %% [markdown]
# 3. Let's display this value in an informative way. Print out the following string in the kernel:
# 
#    ```
#    This person's insurance cost is {insurance_cost} dollars.
#    ```
#    
#    You will need to use string concatenation, including the `str()` function to print out the `insurance_cost`.

# %%

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# %% [markdown]
# ## Looking at Age Factor

# %% [markdown]
# 4. We have seen how our formula can estimate costs for one individual. Now let's play with some individual factors to see what role each one plays in our estimation!
# 
#    Let's start with the `age` factor. Using a plus-equal operator, add 4 years to our `age` variable.

# %%
age += 4

# %% [markdown]
# 5. Now that we have changed our `age` value, we want to recalculate our insurance cost. Declare a new variable called `new_insurance_cost` in the code block below.
# 
#    Make sure you leave the `insurance_cost` variable the same as in Task 2. We will use it later in our program!

# %%
new_insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500

# %% [markdown]
# 6. Next, we want to find the difference between our `new_insurance_cost` and `insurance_cost`. To do this, let's create a new variable called `change_in_insurance_cost` and set it equal to the difference between `new_insurance_cost` and `insurance_cost`.
# 
#    Note: depending on the order that we subtract (eg., `new_insurance_cost - insurance_cost` vs. `insurance_cost - new_insurance_cost`), we'll get a positive or negative version of the same number. To make this difference interpretable, let's calculate `new_insurance cost - insurance_cost`. Then we can say, "people who are four years older have estimated insurance costs that are `change_in_insurance_cost` dollars different, where the sign of `change_in_insurance_cost` tells us whether the cost is higher or lower".

# %%
change_in_insurance_cost = new_insurance_cost - insurance_cost

# %% [markdown]
# 7. We want to display this information in an informative way similar to the output from instruction 3. In the code block below, print the following string, where `XXX` is replaced by the value of `change_in_insurance_cost`:
# 
#    ```
#    The change in cost of insurance after increasing the age by 4 years is XXX dollars.
#    ```
#    
#    Doing this will tell us how 4 years in age affects medical insurance cost estimates assuming that all other variables remain the same.
#    
#    You will need to concatenate strings and use the `str()` method.

# %%
print("The change in cost of insurance after increasing the age by 4 years is "+str(change_in_insurance_cost)+" dollars.")

# %% [markdown]
# ## Looking at BMI Factor

# %% [markdown]
# 8. Now that you have looked at the age factor, let's move onto another one: BMI. First, we have to redefine our `age` variable to be its original value.
# 
#    Set `age` to `28`. This will reset its value and allow us to focus on just the change in the BMI factor moving forward.
#    
#    On the next line, using the plus-equal operator, add `3.1` to our `bmi` variable.

# %%
age = 28
bmi += 3.1
new_insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500
change_in_insurance_cost = new_insurance_cost - insurance_cost


# %% [markdown]
# 9. Now let's find out how a change in BMI affects insurance costs. Our next steps are pretty much the same as we have done before when looking at `age`.
#    1. Below the line where `bmi` was increased by `3.1`, rewrite the insurance cost formula and assign it to the variable name `new_insurance_cost`.
#    2. Save the difference between `new_insurance_cost` and `insurance_cost` in a variable called `change_in_insurance_cost`.
#    3. Display the following string in the output terminal, where `XXX` is replaced by the value of `change_in_insurance_cost`:
#    
#    ```py
#    The change in estimated insurance cost after increasing BMI by 3.1 is XXX dollars.
#    ```

# %%
print('The change in estimated insurance cost after increasing BMI by 3.1 is ' + str(change_in_insurance_cost) + ' dollars')

# %% [markdown]
# ## Looking at Male vs. Female Factor

# %% [markdown]
# 10. Let's look at the effect sex has on medical insurance costs. Before we make any additional changes, first reassign your `bmi` variable back to its original value of `26.2`.
# 
#     On a new line of code in the code block below, reassign the value of `sex` to `1`. A reminder that `1` identifies male individuals and `0` identifies female individuals.

# %%
bmi = 26.2
sex = 1

# %% [markdown]
# 11. Perform the steps below!
#     1. Rewrite the insurance cost formula and assign it to the variable name `new_insurance_cost`.
#     2. Save the difference between `new_insurance_cost` and `insurance_cost` in a variable called `change_in_insurance_cost`.
#     3. Display the following string, where `XXX` is replaced by the value of `change_in_insurance_cost`:
#     ```
#     The change in estimated cost for being male instead of female is XXX dollars.
#     ```

# %%
new_insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print('The change in estimated cost for being male instead of female is '+ str(change_in_insurance_cost)+ ' dollars.')

# %% [markdown]
# 12. Notice that this time you got a negative value for `change_in_insurance_cost`. Let's think about what that means. We changed the sex variable from `0` (female) to `1` (male) and it decreased the estimated insurance costs.
# 
#     This means that men tend to have lower medical costs on average than women. Reflect on the other findings you have dug up from this investigation so far.

# %%


# %% [markdown]
# ## Extra Practice

# %% [markdown]
# 13. Great job on the project!!!
# 
#     So far we have looked at 3 of the 5 factors in the insurance costs formula. The two remaining are `smoker` and `num_of_children`. If you want to keep challenging yourself, spend some time investigating these factors!
#     1. Rewrite the insurance cost formula and assign it to the variable name `new_insurance_cost`.
#     2. Save the difference between `new_insurance_cost` in a variable called `change_in_insurance_cost`.
#     3. Display the information below!

# %%
age=28
bmi=26.2
sex=0
#smoker
num_of_children=3
smoker=1
new_insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print('Being a smoker changes the cost of insurance by '+ str(change_in_insurance_cost)+' dollars.')

# %%
#children
smoker=0
num_of_children+=1
new_insurance_cost = (250*age) - (128*sex) + (370*bmi) + (425*num_of_children) + (24000*smoker) -12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print('Having one more child changes the cost of insurance by '+ str(change_in_insurance_cost)+' dollars.')


