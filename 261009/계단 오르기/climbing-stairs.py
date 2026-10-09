N = int(input())

dp = [0] * (N+1)
if N >= 2:
    dp[2] = 1
if N >= 3:
    dp[3] = 1

for i in range(4, N + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

if dp[N]==0:
    print(0)
else:
    print(dp[N]%10007)