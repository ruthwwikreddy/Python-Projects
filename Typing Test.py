import time
import random

test_sentences = [
    "Reading books broadens our horizons and enriches our mind.",
    "The early bird catches the worm, but the second mouse gets the cheese.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold; often have you heard that told.",
    "Where there's a will, there's a way.",
    "Knowledge is power, and power is responsibility.",
    "The pen is mightier than the sword.",
    "Actions speak louder than words.",
    "A picture is worth a thousand words.",
    "Necessity is the mother of invention.",
    "When in Rome, do as the Romans do.",
    "The only way to do great work is to love what you do.",
    "Stay hungry, stay foolish.",
    "Imagination is more important than knowledge.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "In the middle of difficulty lies opportunity.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Be the change you wish to see in the world.",
    "Simplicity is the ultimate sophistication.",
    "The only limit to our realization of tomorrow will be our doubts of today."
    "The quick brown fox jumps over the lazy dog.",
    "Typing speed tests help improve accuracy and speed.",
    "Python is a versatile and widely used programming language.",
    "Artificial intelligence is transforming the world.",
    "Practice makes perfect in everything you do.",
    "Success comes to those who are willing to work for it.",
    "The rain in Spain stays mainly in the plain.",
    "Consistency is the key to mastering any skill.",
    "A journey of a thousand miles begins with a single step.",
    "Time and tide wait for no man.",
    "Good things come to those who wait, but better things come to those who work for it.",
    "Innovation distinguishes between a leader and a follower.",
    "You miss one hundred percent of the shots you don't take.",
    "The best way to predict the future is to create it.",
    "Life is ten percent what happens to us and ninety percent how we react to it.",
    "Learning never exhausts the mind, and the more we learn, the better we grow.",
    "Believe you can and you're halfway there.",
    "Programming allows us to solve complex problems efficiently.",
    "Small daily improvements lead to stunning results over time.",
    "Reading books broadens our horizons and enriches our mind."
]

test_sentence = random.choice(test_sentences)
print("Type the following sentence as fast as you can:")
print(f"Sentence: {test_sentence}")

input("Press Enter when you are ready...")

start_time = time.time()

user_input = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words_in_sentence = len(test_sentence.split())
words_per_minute = (words_in_sentence / time_taken) * 60

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Your typing speed is: {words_per_minute:.2f} words per minute")

if user_input == test_sentence:
    print("Your typing accuracy is: 100%")
else:
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(test_sentence) and c == test_sentence[i])
    accuracy = (correct_chars / len(test_sentence)) * 100
    print(f"Your typing accuracy is: {accuracy:.2f}%")