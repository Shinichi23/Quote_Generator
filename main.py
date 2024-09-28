import pyquotegen

categories = ["motivational", "friendship", "technology", "inspirational", "funny", "nature", "success", "attitude", "coding"]

print("Choose a categrory : 🚀 motivational,👬 friendship,💻 technology,💡 inspirational,😂 funny,🍃 nature,📈 success,💪 attitude,⌨️ coding")

while True:
    tag = input("Enter the category: ")
    if tag in categories:
        quote = pyquotegen.get_quote(tag)
        print(quote)
        yes_not = input("Do you want another quote? (yes/no): ").strip().lower()
        if yes_not == 'no':
            break

           


