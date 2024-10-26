from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html', data=None)  # Pass None initially

@app.route('/', methods=['POST']) 
def generate_qr():  
    link = request.form['link']  # Get the link from the form
    
    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save it to a BytesIO object
    img_bytes = BytesIO()
    img.save(img_bytes)
    
    # Convert the image to a base64 string
    img_bytes.seek(0)
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    img_data = f"data:image/png;base64,{img_base64}"

    # Render the template with the image data
    return render_template('index.html', data=img_data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


