import keyboard

i = 1
option = 0
owo = {'l':'1', 'z':'2', 'e':'3', 'a':'4', 's':'5', 'g':'6', 't':'7', 'b':'8', 'p':'9', 'o':'0'}


def check_for_caps_lock(e, hook_on_press):
    global i
    if e.name.lower() == 'caps lock':
        keyboard.unhook(hook_on_press)
        i = 0
        return


def check_for_movement_key(e):
    for move_key in {'space', 'tab', 'backspace', 'caps lock', 'esc', 'enter'}:
        if e.name.lower() == move_key:
            keyboard.send(e.name)
            return False
    else:
        return True


def odd_numbers(e, hook_on_press):
    global i
    check_for_caps_lock(e, hook_on_press)
    if check_for_movement_key(e):
        if not keyboard.is_modifier(e.name):
            if i % 2:
                keyboard.write(e.name.upper())
            else:
                keyboard.write(e.name.lower())
        else:
            i -= 1
    i += 1


def owo_lang(e, hook_on_press):
    check_for_caps_lock(e, hook_on_press)
    if check_for_movement_key(e):
        if not keyboard.is_modifier(e.name):
            if e.name.isalpha():
                if e.name.isupper():
                    if e.name.lower() == 'l' or e.name.lower() == 'r':
                        keyboard.write('w')
                    else:
                        keyboard.write(e.name.lower())
                else:
                    if e.name.lower() == 'l' or e.name.lower() == 'r':
                        keyboard.write('W')
                    else:
                        keyboard.write(e.name.upper())
            else:
                keyboard.write(e.name)


def num_lang(e, hook_on_press):
    check_for_caps_lock(e, hook_on_press)
    if check_for_movement_key(e):
        if not keyboard.is_modifier(e.name):
            if e.name.isalpha():
                for key in owo:
                    if e.name.lower() == key:
                        keyboard.write(owo[key])
                        return
                if e.name.isupper():
                    keyboard.write(e.name.lower())
                    return
                else:
                    keyboard.write(e.name.upper())
                    return
            else:
                keyboard.write(e.name)
                return


def caps_lock_1():
    hook_on_press = keyboard.on_press(lambda e: odd_numbers(e, hook_on_press), True)
    keyboard.wait('caps lock')


def caps_lock_2():
    hook_on_press = keyboard.on_press(lambda e: owo_lang(e, hook_on_press), True)
    keyboard.wait('caps lock')


def caps_lock_3():
    hook_on_press = keyboard.on_press(lambda e: num_lang(e, hook_on_press), True)
    keyboard.wait('caps lock')


def set_option(tmp):
    global option
    option = tmp


def main():
    global option
    while True:
        option = 0
        keyboard.add_hotkey('caps lock+1', lambda: set_option(1), suppress=True)
        keyboard.add_hotkey('caps lock+2', lambda: set_option(2), suppress=True)
        keyboard.add_hotkey('caps lock+3', lambda: set_option(3), suppress=True)
        keyboard.add_hotkey('ctrl+caps lock+esc', lambda: set_option(10), suppress=True)
        keyboard.read_key()

        if option == 1:
            caps_lock_1()
        if option == 2:
            caps_lock_2()
        if option == 3:
            caps_lock_3()
        if option == 10:
            break


if __name__ == '__main__':
    main()
