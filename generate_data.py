import numpy as np
import pandas as pd


def generate_random_data(n_cells:int, n_genes:int, file_name:str) -> None:
    """Generate a toy parquet file

    Args:
        - n_cells (int) : number of cells (rows)
        - n_genes (int) : number of genes
        - file_name (str) : name of the file to save (sould be a .parquet file)
    
    """

    # get cols names
    gene_names = [f"Gene_{i+1}" for i in range(n_genes)]

    # generate random gene expressions
    expression = np.abs(np.random.randn(n_cells, n_genes) * 2)

    # create datafarame
    df = pd.DataFrame(expression, columns=gene_names)

    # add cell id
    df['ID'] = [f"cell_{i+1}" for i in range(n_cells)]

    # add random labels
    cell_types = ["T_cell", "B_cell", "Monocyte", "NK_cell"]
    df["LABEL"] = np.random.choice(cell_types, size=n_cells)

    # save
    df.to_parquet(file_name, index=False)



if __name__ == "__main__":

    generate_random_data(100, 10, "data/toy.parquet")


    
