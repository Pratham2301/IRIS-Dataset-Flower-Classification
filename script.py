import pickle

# INPUT
print("\n\nPlease Enter Details : \n\n")
sepal_len = int(input("Sepal Length : "))
sepal_wid = int(input("Sepal width : "))
petal_len = int(input("Petal Length : "))
petal_wid = int(input("Petal width : "))


# opening pickle file in read mode
file = "model.pkl"
fileobj = open(file, 'rb')

# accessing model
model = pickle.load(fileobj)

# prediction
output = model.predict([[sepal_len, sepal_wid, petal_len, petal_wid]])

# OUTPUT
target_names = ['setosa', 'versicolor', 'virginica']
index = output[0]

print("\nClassified Flower : ", target_names[index], "\n\n")
