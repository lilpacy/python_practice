from perceptron import *

# これでは[0,1,1,0]のXORゲートが表現できない
# AND,NAND,ORを組み合わせてXORゲートを実装する

def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y

print(XOR(0,0),XOR(0,1),XOR(1,0),XOR(1,1))

