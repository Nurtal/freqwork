import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

def train_decision_tree(parquet_path:str, model_out:str) -> None:
    """
    Entraîne un arbre de décision à partir d'un fichier parquet et sauvegarde le modèle.
    
    Args :
        - parquet_path (str) : path to parquet input data file
        - model_out (str) : file name to save the model (.pkl).
        
    """
    
    # Load data
    df = pd.read_parquet(parquet_path)
    X = df.drop(columns=['LABEL'])
    y = df['LABEL']
    
    # create and fit clf
    clf = DecisionTreeClassifier()
    clf.fit(X, y)
    
    # save model
    joblib.dump(clf, model_out)


if __name__ == "__main__":

    train_decision_tree("data/toy.parquet", "model/toy_tree.pkl")
