import pyquotegen

categories = ["motivational", "friendship", "technology", "inspirational", "funny", "nature", "success", "attitude", "coding"]

while True:
    print("🚀 motivational,👬 friendship,💻 technology,💡 inspirational,😂 funny,🍃 nature,📈 success,💪 attitude,⌨️ coding")
    tag = input("Enter the category: ")
    if tag in categories:
        quote = pyquotegen.get_quote(tag)
        print(quote)
        while True:
            yes_not = input("Do you want another quote? (yes/no): ").strip().lower()
            if yes_not == 'yes':
                break  # Go back to the beginning of the outer loop
            elif yes_not == 'no':
                print("Goodbye!")
                exit()  # Exit the program
            else:
                print("Please answer with 'yes' or 'no'.")
    else:
        print("Invalid category. Please try again.")
