def check_email(string):
    con_1 = " " not in string
    con_2 = "@" in string
    con_3 = "." in string[string.find("@") + 2:]

    return con_1 and con_2 and con_3
