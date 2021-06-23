import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from six import StringIO
import pydotplus
import pickle

def read_dataset():
    df = pd.read_csv('exasens.txt', sep=",", header=None,
                     names=["Diagnosis", "IP(min)", "IP(avg)", "RP(min)", "RP(avg)", "Gender", "Age", "Smoking"])
    return df

def TreeClassifier(df):
    x = df.loc[:, 'IP(min)':'Smoking']
    y = df['Diagnosis']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier(criterion='gini', max_depth=5)
    clf = clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    print('Отчет классификации для дерева классификации: \n', classification_report(y_test, y_pred))
    return clf

def save_model(model, filename):
    file = filename
    pickle.dump(model, open(file, 'wb'))
    return True

def image_tree(clf):
    x = df.loc[:, 'IP(min)':'Smoking']
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data, rounded=True,
                    special_characters=True, feature_names=x.columns, class_names=['COPD','HC','Asthma','Infected'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('exasens_tree.png')

if __name__ == "__main__":
    df = read_dataset()
    TreeClassifier(df)