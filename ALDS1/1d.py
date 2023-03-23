n = int(input())
l = [int(input()) for i in range(n)]
print(max([j-min(l[:i]) for i,j in enumerate(l) if i>0]))

# これでもTLE

"""
chatGPTにリファクリングさせたコードがACして自信を喪失した。

n = int(input())
l = [int(input()) for i in range(n)]
min_val = l[0]
max_diff = -1000000000
for i in range(1, n):
    max_diff = max(max_diff, l[i] - min_val)
    min_val = min(min_val, l[i])
print(max_diff)


- ループ処理を1つに減らすため、リスト内包表記ではなく通常のforループを使用します。
- 最小値を探すためのmin関数をforループ内に移動させ、毎回最小値を更新するのではなく、ループを回しながらmin_valを更新していきます。
- 差分の最大値を求めるために、毎回リストをスライスして差分を計算するのではなく、ループを回しながら最小値との差分を計算し、最大値を更新していきます。
"""
