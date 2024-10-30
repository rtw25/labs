from flask import Flask, request, render_template, redirect, url_for
import segno
import os

app = Flask(__name__)

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_message = request.form.get('data')  # Use .get() to avoid KeyError
        if not input_message:
            return "No data provided", 400  # Return an error if no data is found
        
        # Generate QR code
        qr = segno.make(input_message)
        qr_code_path = 'static/qr_code.png'  # Specify the path for the QR code image
        qr.save(qr_code_path)  # Save the QR code image
        
        # Redirect to the result page with the message
        return redirect(url_for('result', message=input_message, qr_code=qr_code_path))

    return render_template('index.html')

@app.route('/result')
def result():
    message = request.args.get('message')
    qr_code = request.args.get('qr_code')
    return render_template('result.html', message=message, qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)
