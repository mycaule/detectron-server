import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from starlette.responses import FileResponse
from detector import detect

app = FastAPI()
logger = logging.getLogger("app")

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/{image_url}")
async def read_item(image_url: str):
    return FileResponse(f"inputs/{image_url}")

models = {
    'coco-detection': ['configs/COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml', 'detectron2://COCO-Detection/faster_rcnn_R_50_FPN_3x/137849458/model_final_280758.pkl'],
    'coco-panoptic': ['configs/COCO-PanopticSegmentation/panoptic_fpn_R_101_3x.yaml', 'detectron2://COCO-PanopticSegmentation/panoptic_fpn_R_101_3x/139514519/model_final_cafdb1.pkl'],
    'coco-instance': ['configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml', 'detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl'],
    'coco-keypoints': ['configs/COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x.yaml', 'detectron2://COCO-Keypoints/keypoint_rcnn_R_101_FPN_3x/138363331/model_final_997cc7.pkl'],
    'lvis-instance': ['configs/LVIS-InstanceSegmentation/mask_rcnn_R_101_FPN_1x.yaml', 'detectron2://LVIS-InstanceSegmentation/mask_rcnn_R_101_FPN_1x/144219035/model_final_824ab5.pkl'],
    'pascal-voc': ['configs/Cityscapes/mask_rcnn_R_50_FPN.yaml', 'detectron2://Cityscapes/mask_rcnn_R_50_FPN/142423278/model_final_af9cf5.pkl']
}

@app.get("/v2/{model_alias}/{image_url}")
async def detect_image(model_alias: str, image_url: str):
    if model_alias in models:
        # See MODEL-ZOO.md for possible pairs
        predictions, vis_output = await detect(image_url, models[model_alias][0], models[model_alias][1])
        instances = predictions['instances']
        # TODO Pipe to response without writing the file
        logger.info(f"{image_url}: detected {len(instances)} instances")
        logger.info(type(vis_output.get_image()))
        # return predictions
        return FileResponse(f"outputs/{image_url}")
    else:
        raise HTTPException(status_code=404, detail=f"Model does not exist: {model_alias}")

@app.put("/v2/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
