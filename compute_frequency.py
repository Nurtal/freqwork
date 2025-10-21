import os
import polars as pl
import compute_gene_order


def write_freq(data_file:str, order:list, positions:list, output_folder:str) -> None:
    """Write frequency files from a data_file

    Args:
        - data_file (str) : path to the parquet file
        - order (list) : computed gene order
        - positions (list) : computed postions of the genes
        - output_folder (str) : path to the output folder
    
    """

    # check output folder
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    # load data
    df = pl.read_parquet(data_file)
    for i in df['ID']:

        # extract values
        dft = df.filter(pl.col('ID') == i).drop(['ID', 'LABEL'])
        dft = dft.select(order)
        vector = dft.to_numpy()[0]

        # write signal
        cmpt = 0
        output_file = open(f"{output_folder}/{i}_freq.csv", "w")
        output_file.write("x,y\n")
        for x in positions:
            output_file.write(f"{x},{vector[cmpt]}\n")
            cmpt+=1
        output_file.close()
        



if __name__ == "__main__":

    r = compute_gene_order.build_random_order("data/toy.parquet")

    write_freq("data/toy.parquet", r['order'], r['positions'], "/tmp/freqtest")


    
