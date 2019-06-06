def string_alternative():
    string1 = input('enter a sentence : ')
    # taking alternative chars starting from first letter with step size 2
    string2 = string1[0::2]
    print(string2)

# calling method from main function
if __name__ == "__main__":
    string_alternative()