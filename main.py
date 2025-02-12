import run_loop as rl
import design
import keyboard
import listener
def main():
    while True:
        record = rl.listen_and_stor_keys()
        characters = record[0]
        design_characters = design.designer(characters)
        print(design_characters)
        if record[1] == ["ctrl" , "shift", "q"]:
            break
main()
