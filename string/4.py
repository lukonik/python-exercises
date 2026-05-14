def join_string(s1: str, s2: str):
    first = s1[0]
    first_2 = s2[0]

    middle = s1[len(s1) // 2]
    middle_2 = s2[len(s2) // 2]

    end = s1[-1]
    end_2 = s2[-1]

    return f"{first}{first_2}{middle}{middle_2}{end}{end_2}"


print(join_string("America","Japan"))