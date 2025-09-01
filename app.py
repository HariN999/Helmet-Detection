from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import os

app = Flask(__name__)

# Load the YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Define helmet-specific classes
classes = ["helmet","nohelmet"]

# Function to perform object detection for helmets
def detect_helmet(image_path):
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_id < len(classes):
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

    # Draw bounding boxes and add labels
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = confidences[i]
        
        color = (0, 255, 0) if label == "helmet" else (0, 0, 255)
        text = f"{label}: {confidence:.2f}"
        
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    output_image_path = "static/detected_image.jpg"
    cv2.imwrite(output_image_path, image)
    return output_image_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        file_path = os.path.join("static", file.filename)
        file.save(file_path)

        # Perform helmet detection
        output_image = detect_helmet(file_path)

        return render_template('index.html', output_image=output_image)

    return render_template('index.html', output_image=None)

if __name__ == "__main__":
    app.run(debug=True)
