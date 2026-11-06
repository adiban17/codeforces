if __name__=="__main__":

    # take input
    equation_string = input()

    # take out the nums and store it in a list
    nums = []
    for char in equation_string:
        if char != '+':
            nums.append(int(char))

    # sort the list in ascending order
    nums.sort()

    # print out the final string
    final_equation = ""
    for idx in range(len(nums)):
        if idx == 0:
            final_equation = final_equation+str(nums[0])
        else:
            final_equation = final_equation + "+" + str(nums[idx])

    print(final_equation)