from .dataset import MyDataset, get_loader


from torch.nn import functional as F
import torch
from torch import nn

def padding_collate_function(batch):
    # Find biggest image
    max_w, max_h = 0, 0

    for img, label in batch:
        w, h = img.shape[1:]

        if max_w < w:
            max_w = w

        if max_h < h:
            max_h = h

    imgs = []
    labels = []
    for img, label in batch:
        # Add padding
        w, h = img.shape[1:]
        pad_w = max_w - w
        pad_h = max_h - h

        pad = (0, pad_h, 0, pad_w)

        new_img = F.pad(img, pad, mode="constant", value=0)
        new_label = F.pad(label, pad, mode="constant", value=0)

        imgs.append(new_img)
        labels.append(new_label)

    imgs = torch.stack(imgs)
    labels = torch.stack(labels)

    return imgs, labels



