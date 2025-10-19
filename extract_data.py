import scanpy as sc
import numpy as np



def extract_data(single_cell_data_file:str, output_parquet_file:str) -> None:
    """Extract data from a h5ad file and save it into a parquet file

    Args:
        - single_cell_data_file (str) : single cell input file, h5ad format
        - output_parquet_file (str) : parquet file to save extracted data
    
    """

    # load data
    adata = sc.read_h5ad(single_cell_data_file)
    expr = adata.X
    
    # WARINING this take a lot of computer power
    # convert to dataframe
    if not isinstance(expr, np.ndarray):
        expr = expr.toarray()
    df = pd.DataFrame(expr, index=adata.obs_names, columns=adata.var_names)

    # add cell type as label
    df["label"] = adata.obs["cell_type"].values

    # save data
    df.to_parquet(output_parquet_file)
    




if __name__ == "__main__":

    extract_data("data/zheng_train.h5ad", "data/train.parquet")
    
