
def str_to_int(s):
    s = s.strip()

    if s == '':
        return 0

    sign = "plus"
    if s[0] == "+":
        s = s[1:]
        sign = "plus"
    elif s[0] == "-":
        s = s[1:]
        sign = "neg"
    else:
        pass


    integers = list("0123456789")
    num_str = ""
    # start = None
    # first_flag = False
    # # gets the first num value
    # for i, c in enumerate(s):
    #     if c in integers:
    #         num_str += c
    #         if first_flag==False and start == None:
    #             first_flag = True
    #             start = i

    #     else:
    #         if first_flag ==True:
    #             break
    # s = s[start:i+1]

    # integer = int(s)

    for i, c in enumerate(s):
        if c not in integers:
            break
        else:
            num_str += c


    integer = int(num_str)

    integer = min(integer, 2147483648-1)
    integer = max(integer, -2147483648)

    if sign == "neg":
        return integer*-1
    else:
        return integer