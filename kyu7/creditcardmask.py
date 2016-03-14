# return masked string
def maskify(cc):
    cc_list = list(cc)
    length = len(cc_list)
    if length < 5:
        for i in range(length):
                cc_list[i] = "#"
    else:
        for i in range((length - 4), length):
                cc_list[i] = "#"
    return "".join(cc_list)