from cryptocurrency_genesis import *
from cryptocurrency_new_block import *

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    blocks_to_add = next_block(previous_block)
    blockchain.append(blocks_to_add)
    # ↓の一文を抜くと、previous_blockが更新されず0番目に対してひたすらnext_block関数を繰り返すだけになる
    previous_block = blocks_to_add
    print("Block {} has been added to the blockchain!".format(blocks_to_add.index))
    print("Hash: {}\n".format(blocks_to_add.hash))

print(blockchain)
# previous_block更新の1行を抜いてみても、blockchainリストの中には異なるハッシュ値が入っている。それは、timestampだけが実行時刻で更新されているため、別々のハッシュ値が生成されて格納されているからだと考えられる
# いや、全ての値が同じでも作り直すごとに別々のハッシュ値が生成されてないか？
# でも、.hashで取得したハッシュの値は全てのブロックで同じになっているぞ？
# ってことは、同じように見えていて自分の気づいていない違いがそれぞれのブロックにあるってことか？
