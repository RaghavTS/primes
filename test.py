
run = True
while run:
    option = str(input("What do you want bruh?"))
    if 'check' in option:
        import primefinder
        primefinder
    elif 'nothing' in option:
        run = False
    else:
        import prime_generator
        prime_generator
