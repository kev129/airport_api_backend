# airport_api_backend

## Flight Information Checker

### Project Overview

The Flight Information Checker is a web application that provides real-time information about flights and their destinations. Users can search for airports, retrieve scheduled flights, and get details such as departure times, destinations, delays, and weather conditions at the destination.

### Technologies Used

- Flask (Backend Server)
- Python (Programming Language)
- HTML, CSS, JavaScript (Frontend)
- Render.com (Hosting)

### Setup and Deployment

#### Local Setup

1. Clone the repository:

    ```bash
   git clone https://github.com/kev-129/flight-information-checker.git
    ```

2. Install dependencies:

    ```bash
        pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project root with the following:

    ```env
    airport_api_key=your_airport_api_key
    weather_api_key=your_weather_api_key
    ```

4. Run the Flask app:

    ```bash
    python app.py
    ```

    The app will be available at [http://localhost:5000](http://localhost:5000).

#### Deploying on Render.com

1. Create an account on [Render.com](https://render.com/).

2. Create a new web service on Render, and set up the following:

   - **Build Command:** `python app.py`
   - **Environment Variables:** Add your `airport_api_key` and `weather_api_key`.
   - **Port:** Set to `8080`.

3. Deploy the service.

4. Your web service will be live at the provided Render URL.


