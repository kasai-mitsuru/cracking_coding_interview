# 100階のフロアを下からm階つ区切って1コ目の卵を落としていき、どの区間にいるかを特定し、
# その後、2個目の卵を使ってその区間内のどのフロアにあるかを特定することを考える。
# 例）m = 20のとき
# １個目の卵：20階、40階、60階、80階の順で落とす
# →　例えば80階で割れたとすると、60~80階のどこかにNがあることが分かる
# ２個目の卵：60階、61階、...、80階としらみつぶしに落としていく
# →　Nがどの階か正確に分かる
#
# この時、最悪計算量は
# 1個目の卵の最悪計算量: 100/m - 1回ぐらい
# 2個目の卵の最悪計算量：m回
#
# よって、100/m + m -> min とするmが、最小の最悪計算量を与える
#
# f(m) = m + 100/m
# f'(m) = 1 - 100/(m^2)
# m = 10の時f'(m) = 0となりf(m)は最小値となる
#
# よって、m=10、つまり「1つめの卵を10F, 20F, 30F....と落とし、割れたフロアの下の10Fを2つめの卵でしらみ潰しする」が最悪計算量を最小とする
# この時、最悪計算量は
#
# 1つめの卵: 10F, 20F, ..., 90F -> 9回
# 2つめの卵: 91F, 92F, ..., 100F -> 10回
#
# の19回
