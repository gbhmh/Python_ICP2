# taking N student input
num1 = int(input("enter number of students : "))
# input Weights
string1 = input("Enter a list of weights separated by comma ")
# storing input weights into list
myList1 = string1.split(',')
# printing input weights list
print('input list is {}'.format(myList1))
myList2 = []
a = 0

# checking given number of weights equal to number of students or not
if num1==len(myList1):
    # using for loop
    for item in myList1:
        # a = int(item)*0.45359237
        # converting lb to kg
        a = int(item) * 0.4536
        # appending each converted weight to new list
        myList2.append(a)

    print('using for loop output is {}'.format(myList2))

    # using list comprehension
    myList3 = [int(item)*0.4536 for item in myList1]
    print('using list comprehension output is {}'.format(myList3))
else:
    print('please give number of weights equal to number of students')


