from flask import Flask, render_template, request
from weather import get_weather, api_key

app= Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def index():
    data= None
    error= None
    try:
        if request.method == 'POST':
            location = request.form.get('location')
            if location:
                data = get_weather(location, api_key)
                if data is None:
                    error = "Could not retrieve weather data."
            else:
                error = "Location cannot be empty."
    except Exception as e:
        error = f"An error occurred: {str(e)}"
        # Log the exception for further investigation
        app.logger.error(f"Exception occurred: {str(e)}")

    return render_template('index.html', data=data, error=error)

if __name__== '__main__':
    app.run(debug= True)