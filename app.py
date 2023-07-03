from flask import Flask, request, jsonify
from text_recognition import recognize_text

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/text-recognition',methods=['POST'])
def text_recognition():
    # Get the image data from the request
    image_data = request.files['image']
    # Save the image to a temporary file

    temp_image_path = 'images/imgjp.jpeg'
    # print (temp_image_path)
    image_data.save(temp_image_path)

    # # Perform text recognition
    
    # recognized_text = recognize_text('images/imgjp.jpeg')
    recognized_text = recognize_text(temp_image_path)
    # Remove the temporary image file
    # (Optional: Only if you don't need to keep the image)
    # os.remove(temp_image_path)

    # Return the recognized text as a response
    # return "himanshu"
    return jsonify({'text': recognized_text})


if __name__ == '__main__':
    app.run()



