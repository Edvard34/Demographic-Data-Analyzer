import pandas as pd

# Load the dataset
data = pd.read_csv("census_data.csv")

# 1. How many people of each race are represented in this dataset?
race_counts = data['race'].value_counts()

# 2. What is the average age of men?
average_age_men = data[data['sex'] == 'Male']['age'].mean()

# 3. What is the percentage of people who have a Bachelor's degree?
bachelors_percentage = (data['education'] == 'Bachelors').mean() * 100

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
high_income_advanced = (advanced_education & (data['salary'] == '>50K')).mean() * 100

# 5. What percentage of people without advanced education make more than 50K?
no_advanced_education = ~advanced_education
high_income_no_advanced = (no_advanced_education & (data['salary'] == '>50K')).mean() * 100

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = data['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_data = data[data['hours-per-week'] == min_hours_per_week]
min_hours_high_income_percentage = (min_hours_data['salary'] == '>50K').mean() * 100

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_income_percentage = data.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
country_income_percentage = country_income_percentage['>50K'] * 100
highest_percentage_country = country_income_percentage.idxmax()
highest_percentage_value = country_income_percentage.max()

# 9. Identify the most popular occupation for those who earn >50K in India.
india_high_income = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
most_popular_occupation_india = india_high_income['occupation'].mode()[0]

# Print the results
print("Race counts:\n", race_counts)
print("\nAverage age of men:", round(average_age_men, 1))
print("\nPercentage of people with a Bachelor's degree:", round(bachelors_percentage, 1))
print("\nPercentage of people with advanced education making more than 50K:", round(high_income_advanced, 1))
print("\nPercentage of people without advanced education making more than 50K:", round(high_income_no_advanced, 1))
print("\nMinimum number of hours a person works per week:", min_hours_per_week)
print("\nPercentage of people working the minimum number of hours per week who make more than 50K:", round(min_hours_high_income_percentage, 1))
print("\nCountry with the highest percentage of people earning >50K:", highest_percentage_country)
print("Percentage:", round(highest_percentage_value, 1))
print("\nMost popular occupation for people earning >50K in India:", most_popular_occupation_india)
