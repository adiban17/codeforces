if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())

        number_of_digits = 0

        temp = n
        while temp > 0:
            temp = temp // 10
            number_of_digits += 1

        if n <=10:
            print(n)
        else:
            str_num = str(n)
            first_digit = int(str_num[0])
            total = first_digit + ((number_of_digits-1)*9)
            print(total)

                
