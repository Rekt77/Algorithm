def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]

    st = ['A']
    ans = []
    while st:
        print(routes)
        print(ans)
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans

print(solution([["A", "B"], ["B", "A"], ["B", "C"], ["C", "B"]]))