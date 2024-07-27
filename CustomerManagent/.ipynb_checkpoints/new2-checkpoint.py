# import requests
# from bs4 import BeautifulSoup

# URL = 'https://www.microsoft.com/en/mi'

# PAGE= requests.get(URL)

# SOUP=BeautifulSoup(PAGE.content , 'html.parser')

# print(SOUP.body.text)


import pandas as pd
import csv

# Collect data for the first customer
customer_name1 = input("Enter the first customer’s name: ")
customer_rating1 = int(input("Enter the first customer’s rating (1 - 5): "))
customer_feedback1 = input("Enter the first customer’s feedback: ")

# Collect data for the second customer
customer_name2 = input("Enter the second customer’s name: ")
customer_rating2 = int(input("Enter the second customer’s rating (1 - 5): "))
customer_feedback2 = input("Enter the second customer’s feedback: ")

# Collect data for the third customer
customer_name3 = input("Enter the third customer’s name: ")
customer_rating3 = int(input("Enter the third customer’s rating (1 - 5): "))
customer_feedback3 = input("Enter the third customer’s feedback: ")

# Collect data for the fourth customer
customer_name4 = input("Enter the fourth customer’s name: ")
customer_rating4 = int(input("Enter the fourth customer’s rating (1 - 5): "))
customer_feedback4 = input("Enter the fourth customer’s feedback: ")

# Collect data for the fifth customer
customer_name5 = input("Enter the fifth customer’s name: ")
customer_rating5 = int(input("Enter the fifth customer’s rating (1 - 5): "))
customer_feedback5 = input("Enter the fifth customer’s feedback: ")



with open('customer_feedback.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(["Name", "Rating", "Feedback"])
    
    # Write each customer's data
    writer.writerow([customer_name1, customer_rating1, customer_feedback1])
    writer.writerow([customer_name2, customer_rating2, customer_feedback2])
    writer.writerow([customer_name3, customer_rating3, customer_feedback3])
    writer.writerow([customer_name4, customer_rating4, customer_feedback4])
    writer.writerow([customer_name5, customer_rating5, customer_feedback5])




df = pd.read_csv('customer_feedback.csv')


(df)

# Display the first few rows of the dataset
(df.head())


(df.info())



# Calculating total and average rating
total_ratings = df['Rating'].sum()
average_rating = total_ratings / len(df)
print("Average Rating: ", average_rating)



# Categorizing feedback for the first customer
if customer_rating1 >= 5 and "excellent" in customer_feedback1.lower():
    feedback_category1 = "Very Positive"
elif customer_rating1 >= 4:
    feedback_category1 = "Positive"
elif customer_rating1 == 3:
    feedback_category1 = "Neutral"
else:
    feedback_category1 = "Negative"
    
# Categorizing feedback for the second customer
if customer_rating2 >= 5 and "excellent" in customer_feedback2.lower():
    feedback_category2 = "Very Positive" 
elif customer_rating2 >= 4:
    feedback_category2 = "Positive"
elif customer_rating2 == 3:
    feedback_category2 = "Neutral"
else:
    feedback_category2 = "Negative"
    
# Categorizing feedback for the third customer
if customer_rating3 >= 5 and "excellent" in customer_feedback3.lower():
    feedback_category3 = "Very Positive"
elif customer_rating3 >= 4:
    feedback_category3 = "Positive"
elif customer_rating3 == 3:
    feedback_category3 = "Neutral"
else:
    feedback_category3 = "Negative"
    
# Categorizing feedback for the fourth customer
if customer_rating4 >= 5 and "excellent" in customer_feedback4.lower():
    feedback_category4 = "Very Positive"
elif customer_rating4 >= 4:
    feedback_category4 = "Positive"
elif customer_rating4 == 3:
    feedback_category4 = "Neutral"
else:
    feedback_category4 = "Negative"

# Categorizing feedback for the fifth customer
if customer_rating5 >= 5 and "excellent" in customer_feedback5.lower():
    feedback_category5 = "Very Positive"
elif customer_rating5 >= 4:
    feedback_category5 = "Positive"
elif customer_rating5 == 3:
    feedback_category5 = "Neutral"
else:
    feedback_category5 = "Negative"




feedback_categories = [feedback_category1, feedback_category2, feedback_category3, feedback_category4, feedback_category5]
print("Feedback Categories:", feedback_categories)



# Analyzing feedback comments
feedback_words1 = customer_feedback1.lower().split()
feedback_words2 = customer_feedback2.lower().split()
feedback_words3 = customer_feedback3.lower().split()
feedback_words4 = customer_feedback4.lower().split()
feedback_words5 = customer_feedback5.lower().split()

# Counting occurrences of a specific word
word_to_count = "service"
word_count1 = feedback_words1.count(word_to_count)
word_count2 = feedback_words2.count(word_to_count)
word_count3 = feedback_words3.count(word_to_count)
word_count4 = feedback_words4.count(word_to_count)
word_count5 = feedback_words5.count(word_to_count)

print(f"Count of '{word_to_count}' in first feedback:", word_count1)
print(f"Count of '{word_to_count}' in second feedback:", word_count2)
print(f"Count of '{word_to_count}' in third feedback:", word_count3)
print(f"Count of '{word_to_count}' in fourth feedback:", word_count4)
print(f"Count of '{word_to_count}' in fifth feedback:", word_count5)

