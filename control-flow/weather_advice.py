user = input("What's the weather like today? (sunny/rainy/cold): ")
# Prompts the user for input

if user.lower() == "sunny": # Executes if the weather is sunny
    print("Wear a t-shirt and sunglasses.")
elif user.lower() == "rainy": # Executes if the weather is rainy
    print("Don't forget your umbrella and a raincoat.")
elif user.lower() == "cold": # Executes if the weather is cold
    print("Make sure to wear a warm coat and a scarf.")
else: # Executes if the above codes don't get executed
    print("Sorry, I don't have recommendations for this weather.")
