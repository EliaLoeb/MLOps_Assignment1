from pathlib import Path
from typing import Dict, Tuple
import numpy as np
from torch.utils.data import DataLoader
from torchvision import transforms
import torch
from .pcam import PCAMDataset


def get_dataloaders(config: Dict) -> Tuple[DataLoader, DataLoader]:
    """
    Factory function to create Train and Validation DataLoaders
    using pre-split H5 files.
    """
    data_cfg = config["data"]
    base_path = Path(data_cfg["data_path"])

    # TODO: Define Transforms
    # train_transform = ...
    # val_transform = ...

    # TODO: Define Paths for X and Y (train and val)
    
    # TODO: Instantiate PCAMDataset for train and val

    # TODO: Create DataLoaders
    # train_loader = ...
    # val_loader = ...
    train_transform = transforms.Compose([
        transforms.ToTensor(),
    ])
    val_transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    train_x_path = base_path / "camelyonpatch_level_2_split_train_x.h5"
    train_y_path = base_path / "camelyonpatch_level_2_split_train_y.h5"
    val_x_path = base_path / "camelyonpatch_level_2_split_valid_x.h5"
    val_y_path = base_path / "camelyonpatch_level_2_split_valid_y.h5"
    test_x_path = base_path / "camelyonpatch_level_2_split_test_x.h5"

    train_dataset = PCAMDataset(str(train_x_path), str(train_y_path), transform=train_transform)
    val_dataset = PCAMDataset(str(val_x_path), str(val_y_path), transform=val_transform)

    labels = train_dataset.labels[:]
    class_sample_count = np.array([len(np.where(labels == t)[0]) for t in np.unique(labels)])
    weight = 1. / class_sample_count
    samples_weight = np.array([weight[int(t)] for t in labels]).flatten()
    samples_weight = torch.from_numpy(samples_weight)
    
    sampler = WeightedRandomSampler(samples_weight.type('torch.DoubleTensor'), len(samples_weight))

    train_loader = DataLoader(
        train_dataset, 
        batch_size=data_cfg["batch_size"], 
        sampler=sampler,
        num_workers=data_cfg.get("num_workers", 0)
    )
    
    val_loader = DataLoader(
        val_dataset, 
        batch_size=data_cfg["batch_size"], 
        shuffle=False,
        num_workers=data_cfg.get("num_workers", 0)
    )
    
    return train_loader, val_loader
