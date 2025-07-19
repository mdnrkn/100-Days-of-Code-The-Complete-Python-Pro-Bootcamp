def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")

    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")

    first_digit = t + r + u + e
    second_digit = l + o + v + e

    score = (int(str(first_digit) + str(second_digit)))
    print(f"{score}%")

calculate_love_score("Alice", "Bob")