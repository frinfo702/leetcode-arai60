# step1
- O(log(N)) N:　numsの長さ　から二分探索を使うと考えた。時間計算量の指定が問題文にあるのでこの解法に飛びついたが無理そうならまた別のものを試そうと一旦この解法でやってみた
- 初めは`while left_index != right_index:`と書いていたがleft, right_indexが必ずleft_index < right_indexの関係を保持したままその差を小さくしていくなら`<`でいいので書き直した
- 正確にはleft_index <= right_indexが常に成り立つが等号成立時をループの終了として判定したいので`<`とした
- まず入力は昇順にソートされた配列の要素をいくつかずらし、はみ出た要素は先頭に持ってくる(この操作を回転と呼んでいる)ことを繰り返すことでできる配列
- left_index, right_indexはそれぞれ探索対象の配列の左端、右端のインデックス
- 探索対象の配列というのは、最小値が入っていると推測される部分配列のこと
- left_index, right_indexは最小値が見つかるまで必ずleft_index < right_indexという関係を崩さない
- left_indexがright_indexと等しくなった時left_indexかright_indexのインデックスに対応する要素を返

## 探索対象の配列の判断
- nums[mid_index] > nums[right]なら左半分は昇順にソートされた部分配列で回転の結果、最小値は配列の中央のインデックスを超えて右半分にあると判断
- nums[mid_index] <= nums[left_index]なら同様に左半分に最小値が含まれていると判断


3 4 5 6 1 2
6 1 2 3 4 5
# step2
