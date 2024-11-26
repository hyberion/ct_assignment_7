#Task 1- Keyword Highligher
#Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We aim to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
#So it is written, so it shall be done
#Those who are not enthusiastic will be reported and adjusted accordingly

#First Version

#We define the list of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it.",
    "It made a noise that frightened my cat and made me want to stick a fork in my eye.",
    "It was a good product, but the customer service was terrible. It almost made me into a dissenter.",
    "I cried when I turned it on. I heard the screams of chaos. But otherwise it was satisfactory.",
    "WE ARE XENOS. WE ARE COMING. YOUR TERRIBLE PRODUCTS WILL NOT STOP US. OUR HERESY WILL BECOME YOUR RULE.",
    "Not bad.  Left a strange taste in the mount, but didn't seem to cause me to become a traitor."
]

# We define the keywords we want to search for
keywords=["good","excellent","bad","poor","average","made me want to stick a fork in my eye"]

# For task two we generate a list of positive and negative keywords-  We look for the fingerprints of the dissenter.  They must be brought to the light
# all ail the omnisiaah.  We also look for suspicious words.  These are the signs of the xenos, the heritical.
# Innocence is not a defense.  The Emperor Protects

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
suspicious_words = ["average", "mediocre", "okay", "decent", "satisfactory", "chaos", "heresy", "xenos", "dissenter", "dissident", "traitor", "heretic"]

#We make our task two function here.  Because if we put it somewhere else we could lose it.  And that would be bad
def count_sentiment_words(review, positive_words, negative_words, suspicious_words):
    positive_count = 0
    negative_count = 0
    suspicious_count = 0

    for word in review.split():
        if word.lower() in positive_words:
            positive_count += 1
        elif word.lower() in negative_words:
            negative_count += 1
        elif word.lower() in suspicious_words:
            suspicious_count += 1
    return positive_count, negative_count, suspicious_count

#We process each review to look for the heretics that live amungst us.  They must be brought to the light

for review in reviews:
    modified_review = review
    for keyword in keywords:
        if keyword in review:
            modified_review = modified_review.replace(keyword, keyword.upper())
    #Count the number of positive, negative, and suspicious words in the review
    positive_count, negative_count, suspicious_count = count_sentiment_words(review, positive_words, negative_words, suspicious_words)

    print(f"Review: {modified_review}")
    print(f"Positive words: {positive_count}")
    print(f"Negative words: {negative_count}")
    print(f"Suspicious words: {suspicious_count}")
    print("-" * 50)
#We have completed our task.  The heretics have been brought to the light.  The xenos have been exposed.  
# The Inquisition is always watching.  The Emperor Protects