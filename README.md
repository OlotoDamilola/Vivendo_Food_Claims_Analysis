# Vivendo_Food_Claims_Analysis
# Cleaning and Analyzing data in SQL, Power query, Power BI and Python
# Introduction
This project is my Data Analyst Associate Practical Exam organized by DataCamp. I analyzed a dataset provided by DataCamp about food poisoning compensation at Vivendo. Vivendo is a fast food chain in Brazil with over 200 outlet. Customers often claim compensation from the company for food poisoning. The legal team processes these claims and has offices in four locations. The legal team wants to improve how long it takes to reply to customers and close claims. The head of the legal department wants a report on how each location differs in the time it takes to close claims. The dataset contained 2000 cases of food claims and 8 columns which included information about claim_amount, time_to_close, location and cause.  
# Data Cleaning and Manipulation
After downloading and importing the data into MySQL workbench, i checked for missing values and if the values match the description given for all columns. Amount Paid column were not represented in currency of Brazil and there were 36 missing values. Currency was added to all values and the missing values were replaced with the median values of the remaining data, which was R$ 19286.44. Linked cases are either TRUE or FALSE and there were 26 missing values. All missing values were replaced with FALSE.
# Data Preprocessing 
After importing the data into power query, I checked for validity of my data using column distribution, quality and profiling. I noticed the cause column contained either meat, vegetable or unknown. Vegetable were represented in all lower and upper case. All upper case were changed to lower case. In some cases, the first letter in meat were in upper case, all meat were changed to lower case for consistency.
# Data Analysis & Visualizations
1)  Create a visualization that shows the number of claims in each location. Use the visualization to state which category of the variable location has the most observations and explain     whether the observation are balanced across categories of the variable location.

    ![claims_count](https://github.com/OlotoDamilola/Vivendo_Food_Claims_Analysis/assets/109422215/8070ba25-489d-4923-a6d0-8f2546afb280)

    There are four possible locations included in this data. Recife is the most common location customers file claims for compensation for food poisoning with Sao Luis coming in second      with 41% lower rate. The categories are unbalanced, with most observations being Recife and the lowest at Natal. The legal team should concentrate more on improving days to close        claims at Recife as they are more common.

2)  Describe the distribution of time to close for all claims. Your answer must include a visualization that shows the distribution.

    As the legal team wants to improve how long it takes to reply customers and close claims, it is important to look at how days is distributed across locations. Looking at the graphic     below, we can see that most locations have had less than 180 days to reply to customers and close claims. The distribution is too close to being symmetrical, therefore it is             considered to have zero skew. There are some outliers that take less than 80 days and take more than 350 days respectively but this is very uncommon. 

    ![days_distr](https://github.com/OlotoDamilola/Vivendo_Food_Claims_Analysis/assets/109422215/7155f5aa-a202-4293-825c-c061bbc1957c)

3)  Describe the relationship between time to close and location. Your answer must include a visualization to demonstrate the relationship.

    Finally we want to combine the two pieces of information to see how the location impacts the number of days to close claims. So far Recife has collected the most claims but we need      to look at the two variables together. When looking at just the days, we excluded the outlying values so that we could see the majority of the data. To show the impact, we can look      at the range of number of days by location with the outliers in the data. In the graphic below, the outliers are dominating the data and making it difficult to compare the rest of       the data. Sao Luis and Fortaleza had the highest day to close claims, but Recife had the highest number of outliers. To make it easier to compare the rest of the data, we will           remove the outliers.

    ![box_plot_outliers](https://github.com/OlotoDamilola/Vivendo_Food_Claims_Analysis/assets/109422215/909efb27-4f65-468b-9ae0-2be0ce4a6425)

    After we remove the outliers, we can focus on the main range of data. Although Recife is the location with most claims, the interquartile range of the number of days is largest for      Fortaleza and Natal. This would suggest that compared to other locations, Fortaleza and Natal take fewer days to close claims.

    ![box_plot_rmv_outliers](https://github.com/OlotoDamilola/Vivendo_Food_Claims_Analysis/assets/109422215/d05ea421-ae9a-4fd8-8c25-c3f947d83dd4)

# Conclusions
Since the legal department wants a report on how each location differs in the time it takes to close claims, the following conclusions were driven
1)  Recife is the most common location customers file claims for compensation for food poisoning
2)  Most locations have had less than 180 days to reply to customers and close claims
3)  Fortaleza and Natal are the locations where it takes the least time to respond to customers and close claims.

# Recommendations
1)  The legal team should target locations recording over 180 days when trying to improve days it takes to close claims, but keep in mind they might need to work with 186 days.
2)  We would recommend that the legal team focus on improving time to close claims at Recife as it is the location with most claims but also keep an open mind to Sao Luis.
3)  The legal team may think about enforcing a range of days to close cases to avoid having extreme days

