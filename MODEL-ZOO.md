### Detectron2 Model Zoo

Extracted from https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md

### COCO Object Detection Baselines
```
--config-file configs/COCO-Detection/faster_rcnn_R_50_C4_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_C4_1x/137257644/model_final_721ade.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_50_DC5_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_DC5_1x/137847829/model_final_51d356.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_FPN_1x/137257794/model_final_b275ba.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_50_C4_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_C4_3x/137849393/model_final_f97cb7.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_50_DC5_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_DC5_3x/137849425/model_final_68d202.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_101_C4_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_101_C4_3x/138204752/model_final_298dad.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_101_DC5_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_101_DC5_3x/138204841/model_final_3e0943.pkl
--config-file configs/COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_R_101_FPN_3x/137851257/model_final_f6e8b1.pkl
--config-file configs/COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x/139173657/model_final_68b088.pkl
--config-file configs/COCO-Detection/retinanet_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/retinanet_R_50_FPN_1x/137593951/model_final_b796dc.pkl
--config-file configs/COCO-Detection/retinanet_R_50_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/retinanet_R_50_FPN_3x/137849486/model_final_4cafe0.pkl
--config-file configs/COCO-Detection/retinanet_R_101_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/retinanet_R_101_FPN_3x/138363263/model_final_59f53c.pkl
--config-file configs/COCO-Detection/rpn_R_50_C4_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/rpn_R_50_C4_1x/137258005/model_final_450694.pkl
--config-file configs/COCO-Detection/rpn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/rpn_R_50_FPN_1x/137258492/model_final_02ce48.pkl
--config-file configs/COCO-Detection/fast_rcnn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Detection/fast_rcnn_R_50_FPN_1x/137635226/model_final_e5f7ce.pkl
```

### COCO Instance Segmentation Baselines with Mask R-CNN

Object segmentation.
```
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x/137259246/model_final_9243eb.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_1x/137260150/model_final_4f86c3.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x/137260431/model_final_a54504.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_C4_3x/137849525/model_final_4ce675.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_DC5_3x/137849551/model_final_84107b.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_C4_3x/138363239/model_final_a2914c.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_DC5_3x/138363294/model_final_0464b7.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x/138205316/model_final_a3ec72.pkl
--config-file configs/COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_3x/139653917/model_final_2d9806.pkl
```

### COCO Person Keypoint Detection Baselines with Keypoint R-CNN

Similar to Posenet.

```
--config-file configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x/137261548/model_final_04e291.pkl
--config-file configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Keypoints/keypoint_rcnn_R_50_FPN_3x/137849621/model_final_a6e10b.pkl
--config-file configs/COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x/138363331/model_final_997cc7.pkl
--config-file configs/COCO-Keypoints/keypoint_rcnn_X_101_32x8d_FPN_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-Keypoints/keypoint_rcnn_X_101_32x8d_FPN_3x/139686956/model_final_5ad38f.pkl
```

### COCO Panoptic Segmentation Baselines with Panoptic FPN
```
--config-file configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.yaml --opts MODEL.WEIGHTS detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_50_1x/139514544/model_final_dbfeb4.pkl
--config-file configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_50_3x/139514569/model_final_c10459.pkl
--config-file configs/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml --opts MODEL.WEIGHTS detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_101_3x/139514519/model_final_cafdb1.pkl
```

### LVIS Instance Segmentation Baselines with Mask R-CNN
```
--config-file configs/LVIS-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://LVIS-InstanceSegmentation/mask_rcnn_R_50_FPN_1x/144219072/model_final_571f7c.pkl
--config-file configs/LVIS-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://LVIS-InstanceSegmentation/mask_rcnn_R_101_FPN_1x/144219035/model_final_824ab5.pkl
--config-file configs/LVIS-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x.yaml --opts MODEL.WEIGHTS detectron2://LVIS-InstanceSegmentation/mask_rcnn_X_101_32x8d_FPN_1x/144219108/model_final_5e3439.pkl
```

### Cityscapes & Pascal VOC Baselines
```
--config-file configs/Cityscapes/mask_rcnn_R_50_FPN.yaml --opts MODEL.WEIGHTS detectron2://Cityscapes/mask_rcnn_R_50_FPN/142423278/model_final_af9cf5.pkl
--config-file configs/PascalVOC-Detection/faster_rcnn_R_50_C4.yaml --opts MODEL.WEIGHTS detectron2://PascalVOC-Detection/faster_rcnn_R_50_C4/142202221/model_final_b1acc2.pkl
```
