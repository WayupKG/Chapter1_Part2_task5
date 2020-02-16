def stul(gruppa_a, gruppa_b, gruppa_c):
    stul_a = gruppa_a // 2
    stul_b = gruppa_b // 2
    stul_c = gruppa_c // 2
    print(f"Для первой группы нужен {stul_a} стуля")
    print(f"Для второй группы нужен {stul_b} стуля")
    print(f"Для третой группы нужен {stul_c} стуля")
    res = stul_a + stul_b + stul_c
    print(f"Вам нужен {res} стуля")

stul(31, 40, 50)