# SRE Coworker Frontend

This is the frontend for the SRE Coworker multi-agent application, built with Streamlit.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```
   - On Windows:
     ```
     .venv\Scripts\activate
     ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the chat web interface with custom options, use the `run.py` script:

```
python run.py --port 8080 --base_url_path sreCowork --host localhost
```

This will run the app at `http://localhost:8080/sreCowork` without opening the browser.

For default settings, you can also use:
```
streamlit run app.py --server.port 8080 --server.baseUrlPath sreCowork
```

## Deployment

To run this Streamlit app on the web (for broader access or production):

### Option 1: Streamlit Cloud (Easiest)
1. Push your code to a GitHub repository.
2. Visit [share.streamlit.io](https://share.streamlit.io).
3. Connect your GitHub account and select this repository.
4. Set the main file path to `app.py`.
5. Click "Deploy" – your app will be live with a public URL.

### Option 2: Heroku
1. Create a `Procfile` in the root directory with:
   ```
   web: streamlit run app.py --server.port $PORT --server.headless true
   ```
2. Ensure `requirements.txt` includes all dependencies.
3. Push to a Heroku app via git and deploy.

### Option 3: Other Platforms
- **AWS/GCP/Azure**: Use their app hosting services with Docker (create a Dockerfile if needed).
- **Local Web Server**: Run `streamlit run app.py --server.port 8501 --server.address 0.0.0.0` to bind to all interfaces, then access via your machine's IP.

For production deployments, consider adding authentication, HTTPS, and monitoring for security and reliability.

## Features

- Chat interface for interacting with the SRE Coworker multi-agent system
- Placeholder for multi-agent responses (to be integrated in future updates)

## Next Steps

- Integrate multi-agent system for SRE tasks
- Add authentication and user management
- Enhance UI/UX to match specific requirements