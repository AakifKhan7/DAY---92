from flask import Flask, render_template, request
import numpy as np
from PIL import Image
from collections import Counter

app = Flask(__name__)

def get_top_colors(image_path, num_colors=10):
    img = Image.open(image_path)
    img_array = np.array(img)
    pixels = img_array.reshape(-1, img_array.shape[-1])
    color_counts = Counter(map(tuple, pixels))
    top_colors = color_counts.most_common(num_colors)
    return top_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            image_path = f'DAY - 92\static\{file.filename}'
            file.save(image_path)
            top_colors = get_top_colors(image_path, num_colors=10)
            return render_template('result.html', top_colors=top_colors)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
