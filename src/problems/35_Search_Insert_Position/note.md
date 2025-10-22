# 問題
- https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=mnfjz87m


# step1
- 右と左でそれぞれ要素を指すポインタ(と言っていいのか)を用意して、左右から狭めるように動かし続ける
- 右のポインタではtargetより小さい値を検知したらright+1を返して終了
- 左のポインタでも同様のことをする
- もし途中でtargetと一致するところがあればそこを返す
- もし`left <= right`が成立しなくなったらright+1のインデックスを返す

