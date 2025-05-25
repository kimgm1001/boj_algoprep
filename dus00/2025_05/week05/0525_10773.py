def main():
    cnt = int(input())
    stack = []

    for _ in range(cnt):
        num = int(input())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    print(sum(stack))

if __name__ == "__main__":
    main()