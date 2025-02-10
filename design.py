def designer(dic):
    designer_txt = ""
    for date, txt in dic.items():
        designer_txt += date
        designer_txt += "\n________________\n\n"
        for char in txt:
            if len(char) == 1:
                designer_txt += char
            elif char == "space":
                designer_txt += " "
            elif char == "enter":
                designer_txt += "\n"
            else:
                designer_txt += f" {char} "
        designer_txt += "\n\n\n"
    return designer_txt