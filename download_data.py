import requests
import os

def download_benchmark_dataset(output_folder):
    """ """

    # parameters
    url_to_destination = {
        "https://huggingface.co/datasets/genbio-ai/cell-downstream-tasks/resolve/main/zheng/zheng_test.h5ad" : f"{output_folder}/zheng_test.h5ad",
        "https://huggingface.co/datasets/genbio-ai/cell-downstream-tasks/resolve/main/zheng/zheng_train.h5ad": f"{output_folder}/zheng_train.h5ad",
        "https://huggingface.co/datasets/genbio-ai/cell-downstream-tasks/resolve/main/zheng/zheng_valid.h5ad": f"{output_folder}/zheng_valid.h5ad"                
    }

    # create output folder of not exist
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)

    # download files
    for url in url_to_destination:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(url_to_destination[url], "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # éviter les keep-alive chunks vides - This part is vibe coded
                        f.write(chunk)


if __name__ == "__main__":

    download_benchmark_dataset("data")
