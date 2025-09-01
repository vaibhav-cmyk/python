def wealtyperson(accounts):
    ans=0
    for account in accounts:
        ans=max(ans,sum(account))
    return ans

accounts=[[1,5],[7,3],[3,5]]
result=wealtyperson(accounts)
print(result)