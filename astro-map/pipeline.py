from loaders.nasa_apod import load_apod
from twist.twist_filter import twist_filter

def run_pipeline():
    img = load_apod()
    result = twist_filter(img)
    print("Pipeline result:", result)

if __name__ == "__main__":
    run_pipeline()
