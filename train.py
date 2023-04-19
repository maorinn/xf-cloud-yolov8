from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="datasets/pavement-cracks/data.yaml", epochs=50,batch=16,imgsz=640,device=0)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://i.328888.xyz/2023/04/17/ieHrRQ.jpeg")  # predict on an image
success = model.export()