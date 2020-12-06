# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import glob
import os
import tqdm

from detectron2.data.detection_utils import read_image
from utils.predictor import Visualization, setup_cfg

async def detect(image_url: str, config_file: str, model_weights: str, model_device = 'cpu'):
    # List of input images
    inputs = [f"inputs/{image_url}"]

    # File or directory to save output visualizations
    outputs = 'outputs/'
    opts = ['MODEL.WEIGHTS', model_weights, 'MODEL.DEVICE', model_device]

    cfg = setup_cfg(config_file, opts)
    visu = Visualization(cfg)

    # Inputs
    if len(inputs) == 1:
        inputs = glob.glob(os.path.expanduser(inputs[0]))
        assert inputs, "The input path(s) was not found"
    for path in tqdm.tqdm(inputs, disable=not outputs):
        img = read_image(path, format="BGR")
        predictions, vis_output = visu.run_on_image(img)

    # Outputs
    if os.path.isdir(outputs):
        assert os.path.isdir(outputs), outputs
        out_filename = os.path.join(outputs, os.path.basename(path))
    else:
        assert len(inputs) == 1, "Please specify a directory with outputs"
        out_filename = outputs
    vis_output.save(out_filename)
    return predictions, vis_output
