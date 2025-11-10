import re
import os
import pandas as pd
import multiprocessing
from time import time as timer
from tqdm import tqdm
import numpy as np
from pathlib import Path
from functools import partial
import requests
import urllib

def download_image(sample_id, image_link, savefolder):
    if isinstance(image_link, str):
        ext = os.path.splitext(Path(image_link).name)[-1]
        filename = f"{sample_id}{ext}"
        image_save_path = os.path.join(savefolder, filename)
        if not os.path.exists(image_save_path):
            try:
                urllib.request.urlretrieve(image_link, image_save_path)
            except Exception as ex:
                print(f'Warning: Not able to download - {image_link}\n{ex}')

def download_images(sample_ids, image_links, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    download_image_partial = partial(download_image, savefolder=download_folder)
    tasks = zip(sample_ids, image_links)
    with multiprocessing.Pool(60) as pool:
        for _ in tqdm(pool.starmap(download_image_partial, tasks), total=len(image_links)):
            pass
        pool.close()
        pool.join()