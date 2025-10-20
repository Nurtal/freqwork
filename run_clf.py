import joblib
import pandas as pd


def run_clf(data_file, model_file) -> list:
    """Load data and model, run and return prediction
    
    Args:
        - data_file (str) : name of the data (parquet) file
        - model_file (str) : name of the model (pkl) file
    
    """

    # load model
    model = joblib.load(model_file)

    # load data
    X = pd.read_parquet(data_file)
    if 'LABEL' in list(X.keys()):
        X = X.drop(columns=['LABEL'])

    # run prediction
    preds = model.predict(X)

    return preds

    



if __name__ == "__main__":


    run_clf("data/toy.parquet", "model/toy_tree.pkl")
