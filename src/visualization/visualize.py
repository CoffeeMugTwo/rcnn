import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

from PIL import Image

from src.data.data_util import get_bbox_for_image


def add_bbox_to_axis(ax,
                     bbox):
    """Draw bounding box on image.

    Parameter
    ---------
    ax : plt.axis
        Axis with images already inserted.

    bbox : list(float)
        Bbox values. Format: [x, y, width, height]
    """

    rect = patches.Rectangle((bbox[0], bbox[1]),
                             width=bbox[2],
                             height=bbox[3],
                             linewidth=1,
                             edgecolor='r',
                             facecolor='none')

    ax.add_patch(rect)

    return

def plot_image_with_bboxes(image_id,
                           images_folder_path=Path('data/raw/train/'),
                           target_folder_path=Path('data/interim/train/')):
    """Make a plot of the respective image with all bboxes."""
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)

    im = Image.open(images_folder_path / (image_id + '.jpg'))

    ax.imshow(im)

    bbox_list = get_bbox_for_image(image_id)

    for bbox in bbox_list:
        add_bbox_to_axis(ax, bbox)

    fig.savefig(target_folder_path / (image_id + '_bbox.jpg'))

    return


if __name__ == '__main__':
    plot_image_with_bboxes('b6ab77fd7')




