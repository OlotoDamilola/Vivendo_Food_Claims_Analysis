# Vivendo_Food_Claims_Analysis
# Cleaning and Analyzing data in SQL, Power query, Power BI and Python
# Introduction
This project is my Data Analyst Associate Practical Exam organized by DataCamp. I analyzed a dataset provided by DataCamp about food poisoning compensation at Vivendo. Vivendo is a fast food chain in Brazil with over 200 outlet. Customers often claim compensation from the company for food poisoning. The legal team processes these claims and has offices in four locations. The legal team wants to improve how long it takes to reply to customers and close claims. The head of the legal department wants a report on how each location differs in the time it takes to close claims. The dataset contained 2000 cases of food claims and 8 columns which included information about claim_amount, time_to_close, location and cause.  
# Data Cleaning and Manipulation
After downloading and importing the data into MySQL workbench, i checked for missing values and if the values match the description given for all columns. Amount Paid column were not represented in currency of Brazil and there were 36 missing values. Currency was added to all values and the missing values were replaced with the median values of the remaining data, which was R$ 19286.44. Linked cases are either TRUE or FALSE and there were 26 missing values. All missing values were replaced with FALSE.
# Data Preprocessing 
After importing the data into power query, I checked for validity of my data using column distribution, quality and profiling. I noticed the cause column contained either meat, vegetable or unknown. Vegetable were represented in all lower and upper case. All upper case were changed to lower case. In some cases, the first letter in meat were in upper case, all meat were changed to lower case for consistency.
# Data Analysis & Visualizations
1)  Create a visualization that shows the number of claims in each location. Use the visualization to:
    a)  State which category of the variable location has the most observations
    b)  Explain whether the observation are balanced across categories of the variable location

