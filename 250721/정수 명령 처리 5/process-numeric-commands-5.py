N = int(input())

num = []

for _ in range(N):
    arr= input().split()
    command=arr[0]
    if command == "push_back":
        num.append(int(arr[1]))
    elif command=="pop_back":
        num.pop()
    elif command=="size":
        print(len(num))
    elif command=="get":
        print(num[int(arr[1])-1])


