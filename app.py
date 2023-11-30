from flask import Flask, render_template, request
from PIL import Image
from io import BytesIO
import base64
import cv2
import numpy as np
from image_processing import *

# Import các hàm xử lý ảnh từ file xử lý ảnh

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return redirect(request.url)

    file = request.files["file"]

    if file.filename == "":
        return redirect(request.url)

    if file:
        img = Image.open(file)
        img_array = np.array(img)

        # Lấy giá trị của thuật toán từ form
        algorithm = request.form.get("algorithm")

        # Áp dụng thuật toán xử lý ảnh tương ứng
        if algorithm == "negative":
            processed_image = negative_transform(img_array)
        elif algorithm == "threshold":
            processed_image = thresholding_image(img_array)
        elif algorithm == "histogram":
            processed_image = histogram_equalizing(img_array)
        elif algorithm == "logarit":
            processed_image = log_transform(img_array)
        elif algorithm == "otsu":
            processed_image = otsu_algorithm(img_array)
        elif algorithm == "canny":
            processed_image = canny_operator(img_array)
        elif algorithm == "medium":
            processed_image = median_filter(img_array)
        elif algorithm == "average":
            processed_image = average_filter(img_array)
        elif algorithm == "weight":
            processed_image = weighted_averaging(img_array)
        elif algorithm == "laplacian":
            processed_image = laplacian_operator(img_array)
        # Chuyển đổi ma trận NumPy thành ảnh PIL
        pil_image = Image.fromarray(processed_image)

        # Chuyển đổi ảnh PIL thành dạng base64 để hiển thị trên trình duyệt
        buffered = BytesIO()
        pil_image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        img_str = "data:image/png;base64," + base64.b64encode(img_bytes).decode("utf-8")

        return render_template("result.html", img_data=img_str)

if __name__ == "__main__":
    app.run(debug=True)
