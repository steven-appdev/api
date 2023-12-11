from flask import Flask, request, jsonify
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO("model/yolov8n.pt")

@app.route('/predict', methods=['GET'])
def predict():
    if request.method == 'GET':
        detected = ""

        if request.args['imguri'] is None:
            return "<h1>URL not specified!</h1>"
        
        imageURI = request.args['imguri']
        results = model(imageURI)
        result = results[0]
        for box in result.boxes:
            objectDetected = result.names[box.cls[0].item()]
            detected += "<p>"+objectDetected+"</p>"

        return "<h1>Here is what I see</h1>"+detected
if __name__ == "__main__":
    app.run(debug=True)