from typing import Iterable
from sklearn import linear_model
from sklearn import tree
from sklearn.linear_model import RidgeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn import svm
from typing import Literal

class SplitDateset:
    def test_size():
        pass


class ModelSelection:
    def __init__(self, 

    model: Literal["Linear_Model","SVM","Decision_Trees","Neural_Network"],
    
    # Linear Model

    # SVM

    # KNN

    # Decision_Trees
    criterion: Literal["gini","ebtropy"],
    splitter : Literal["best", "random"],
    max_depth = 0,
    max_leaf_nodes = 0

    
    # Neural_Network
    
    ):
        self.model = model
        self.criterion = criterion,
        self.splitter=splitter,
        self.max_depth=max_depth,
        self.max_leaf_nodes=max_leaf_nodes

        self.n = 2 
    
    def model_init(self):
        if self.model == "Linear_Model":
            self.clf = RidgeClassifier()
        elif self.model == "SVM":
            self.clf = svm.SVC()
        elif self.model == "Decision_Trees":
            self.clf = tree.DecisionTreeClassifier(criterion = self.criterion , splitter=self.splitter,max_depth=self.max_depth,max_leaf_nodes=self.max_leaf_nodes )
            print(self.clf.get_params())
        elif self.model == "Neural_Network":
            self.clf = MLPClassifier()

    def model_train(self):
        pass

    def model_test(self):
        pass

    def confustion_matrix(): #reture Yes NO
        pass
    
    




MODEL = ModelSelection(model="Decision_Trees",criterion="gini",splitter="best",max_depth=10 ,max_leaf_nodes=4)
MODEL.model_init()

# def model_selection():
#     pass

# def dataset_sprit():
#     pass

# def taining_model(): 
#     pass

# def model_prediction(): #reture 1 or 0
#     pass

# def confustion_matrix(): #reture Yes NO
#     pass

