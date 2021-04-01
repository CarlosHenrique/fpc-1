
def mochila(T,tam_cano,valores,N):
    for p in tam_cano:
        for v in valores:
            if N == 0 or T == 0:
                return 0
            if p > v:
                return mochila(T,tam_cano[p-1],valores,N)
            else:
                return max(mochila(T,tam_cano[p-1],valores,N),mochila(T-tam_cano[p-1],tam_cano[p-1]+valores[p],valores,N))


def UnboundedKnapsack(Capacity,n,weight,val):
    dp=[]
    for i in range(Capacity+1):
        dp.append(0)
    for i in range(0,Capacity+1):
        for j in range(0,n):
            if weight[j] < i:
                dp[i] = max(dp[i] , dp[i-weight[j]]+val[j])
    return dp[Capacity]