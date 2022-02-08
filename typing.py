def speed_typo():
    "Words to be typed faster"
    global count
    import random
    from datetime import timedelta
    from timeit import default_timer as timer
    words_1 = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]

    print("*******SPEED TYPING GAME*****\n"
          "How first are you?....Let's give it a shot!")

    choice = int(input("How many words do you want to attempt? : "))
    count = 0

    start = timer()
    for x in range(0, choice):
        # the five letter word
        a = random.choice(words_1)
        b = random.choice(words_1)
        c = random.choice(words_1)
        d = random.choice(words_1)
        e = random.choice(words_1)

        # computer manufactured word
        comp_word = a + b + c + d + e
        # *********SPEED TYPING*********
        print(comp_word)
        # user_input word
        user_word = input("your version\n:")

        if user_word == comp_word:
            count += 1
    end = timer()
    time_taken = timedelta(minutes=start - end)

    pass_mark = count / 2

    if count > pass_mark:
        print("Congratulations!, you doing well.")

    else:
        print("Poor. please put more effort")

    print(f"You scored {count} out of {choice} in {time_taken} seconds ")


speed_typo()
