import keyboard
def listen_keys():
    """
    :return: a string of the last character
    """
    if keyboard.read_event().event_type == keyboard.KEY_DOWN:
        return keyboard.read_key()
