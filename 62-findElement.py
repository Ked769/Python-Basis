l = [i for i in input("Enter elements seperated by space : ").split()]
try:
    print(f"Search successful. Item found at index {l.index(input('Enter search term : '))} in the list.")
except ValueError:
    print("Element not found")