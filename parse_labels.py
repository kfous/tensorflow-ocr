import json


def load_annotations(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        annotations  = json.load(f)
    return annotations

if __name__ == '__main__':
    json_path = 'icdar/train_label..json'
    annotations = load_annotations(json_path)
    print("Number of images in JSON:",len(annotations))

    # Check an example
    first_image =list(annotations.keys())[0]
    print("First image:", first_image)
    print("Annotations:", annotations[first_image])