import os
from config import DATA_RAW

def load_local(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    filename = os.path.basename(path)
    target = os.path.join(DATA_RAW, filename)

    with open(path, "rb") as f_in, open(target, "wb") as f_out:
        f_out.write(f_in.read())

    return target
