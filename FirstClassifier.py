## author: Michael John Ambait -- github.com/morfino3
## inspired by: Siraj Raval -- github.com/||Source||
## description: A simple decision tree classifier using scikit-learn's tree that classifies 
## whether a given height, weight and shoe_size are 'male' or 'female' based
## on a dummy data


from sklearn import tree
#[height, weight, shoe_size]
X = [181,80,44], [177,70,43], [160,60,38], [154,54,37], [166,65,40], [190,90,47], [175,64,39], [177,7,40], [159,55,37], [171,75,42], [181,85,43]
Y = ['male','female','female','female','male','male','male','female','male','female','male']
#Y = [0,1,1,1,0,0,0,1,0,1,0]    
clf = tree.DecisionTreeClassifier()


clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction)