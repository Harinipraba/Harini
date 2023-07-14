import random

# Dictionary of quotes by category
quotes = {
    "motivation": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "The only way to do great work is to love what you do. - Steve Jobs"
    ],
    "success": [
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
        "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer"
    ],
    "life": [
        "Life is what happens when you're busy making other plans. - John Lennon",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "The biggest adventure you can take is to live the life of your dreams. - Oprah Winfrey"
    ],
    "love": [
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "The greatest happiness of life is the conviction that we are loved; loved for ourselves, or rather, loved in spite of ourselves. - Victor Hugo",
        "Love isn't something you find. Love is something that finds you. - Loretta Young"
    ]
}

def get_category():
    # Prompt the user to select a category and validate the input
    while True:
        print("Available categories: motivation, success, life, love")
        category = input("Enter a category for the quote: ").lower()
        if category in quotes:
            return category
        else:
            print("Invalid category. Please try again.\n")

def get_name():
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    return name

def personalize_quote(quote, name):
    # Replace the placeholder {name} with the user's name in the quote
    return quote.replace("{name}", name)

def generate_quote():
    # Get user's name and selected category
    name = get_name()
    category = get_category()

    # Retrieve a random quote from the selected category
    quote = random.choice(quotes[category])

    # Personalize the quote with the user's name
    personalized_quote = personalize_quote(quote, name)

    # Display the personalized quote
    print("\nHere's your personalized quote:")
    print(personalized_quote)

# Main program
if __name__ == "__main__":
    generate_quote()
