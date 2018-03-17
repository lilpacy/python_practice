from sigmoid_function import *

X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

print(W1.shape)
print(X.shape)
print(B1.shape)

A1 = np.dot(X,W1)+B1
Z1 = sigmoid(A1)

print(A1,"A1の値")
print(Z1,"Z1の値")

W2 = np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2)+B2
Z2 = sigmoid(A2)

print(A2,"A2の値")
print(Z2,"Z2の値")

def identity_function(x): # 恒等関数の定義
    return x

W3 = np.array([[0.1,0.3],[0.2,0.4]])
B3 = np.array([0.1,0.2])

A3 = np.dot(Z2,W3)+B3
Y = identity_function(A3)

print(A3,"A3の値")
print(Y,"Yの値")
