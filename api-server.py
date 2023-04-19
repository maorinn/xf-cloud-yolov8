#-*-coding:utf-8-*-
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from io import BytesIO
from PIL import Image
import requests
from ultralytics import YOLO
# Load a model
coverModel = YOLO("model/manhole-cover/best.pt")
cracksModel = YOLO("model/pavement-cracks/best.pt")
coverNames = ['closed manhole', 'improperly closed manhole', 'open manhole']
cracksNames = ['alligator cracking', 'edge cracking', 'longitudinal cracking', 'patching', 'pothole', 'rutting', 'transverse cracking']
app = FastAPI()

@app.get('/detect_objects')
async def detect_objects_api(image_url: str, threshold: float = 0.18):
    try:
        predictions = coverModel(image_url,conf=threshold,save_conf=True)  # predict on an image
        det = []
        isIncludeCover = False
        for prediction in predictions:
            prediction_np =  prediction.cpu().numpy()
            current_det = dict()
            cls = prediction_np.boxes.cls
            for cl in cls:
                 cl = int(cl)
                 current_det = dict()
                 current_det['class'] = cl
                 current_det['name'] = coverNames[cl]
                 det.append(current_det)
                 isIncludeCover =True
        # 识别破损路面
        predictions = cracksModel(image_url,conf=threshold,save_conf=True)  # predict on an image、
        isIncludeCracks = False
        for prediction in predictions:
            prediction_np =  prediction.cpu().numpy()
            current_det = dict()
            cls = prediction_np.boxes.cls
            for cl in cls:
                 cl = int(cl)
                 current_det = dict()
                 current_det['class'] = cl
                 current_det['name'] = cracksNames[cl]
                 det.append(current_det)
                 isIncludeCracks = True
        return JSONResponse(content={'detectedObjects': det,'isIncludeCover':isIncludeCover,'isIncludeCracks':isIncludeCracks})
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)
