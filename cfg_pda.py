def main():
    n = int(input("Enter the of Production Rules of CFG: "))
    v = []

    print("Please enter the Production rules of CFG:")

    for _ in range(n):
        s1, s2 = input().split()
        v.append((s1, s2))

    print("The Corresponding Production Rules For PDA are:")
    print("Rules For Non-Terminal Symbols are:")

    for i in range(n):
        flag = 0
        print(f"dl(q,null,{v[i][0]}) --> ", end="")

        check = v[i][1]
        si = len(check)

        ans = ""
        for i in range(si):
            ch = check[i]

            if ch == '|':
                print(f"dl(q,{ans}) |", end="")
                ans = ""
            else:
                ans += ch

        if flag != 1:
            print(f"dl(q,{ans})")

    print("dl(q,0,0) --> dl(q,null)")
    print("dl(q,1,1) --> dl(q,null)")


if __name__ == "__main__":
    main()
