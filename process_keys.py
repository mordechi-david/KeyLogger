import datetime

def date_key(char: str):
    """
    Connects the character with the typing time
    :param char:
    :return:a tuple with time and character
    """
    time = datetime.datetime.now()
    formated_time = time.strftime('%Y.%m.%d  %H:%M')
    return (formated_time, char)

def storing_keystrokes_by_time(char_time: tuple, keystrokes: dict):
    """
    Storing characters sorted by time
    :param char_time: the char to storing
    :param keystrokes: a dictionary to store
    :return: a dictionary that it's keys is the time and the value is a list of characters
    """
    if char_time[0] in keystrokes:
        keystrokes[char_time[0]].append(char_time[1])
    else:
        keystrokes[char_time[0]] = [char_time[1]]
