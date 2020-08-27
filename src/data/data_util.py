from pathlib import Path
import pandas as pd


def get_bbox_for_image(image_id,
                       bbox_file_path=Path('data/raw/train.csv')):
    """Get the bounding boxes for the respective image from the file.

    Parameter
    ---------
    images_id : str
        Id of the image in question

    bbox_file_path : pathlib.Path
        Path to file containing bboxes

    Return
    ------
    bbox_list : list(list(float))
        List of all bboxes. Format: [x_pos, y_pos, width, height]
    """

    df = pd.read_csv(bbox_file_path)

    df_image = df[df["image_id"] == image_id]

    image_bbox = df_image['bbox']

    bbox_list = list()

    for i, bbox_string in image_bbox.iteritems():
        bbox_string = bbox_string.replace('[', '')
        bbox_string = bbox_string.replace(']', '')

        bbox_split = bbox_string.split(',')
        bbox = [float(value) for value in bbox_split]
        bbox_list.append(bbox)

    return bbox_list


if __name__ == '__main__':
    get_bbox_for_image('b6ab77fd7')
