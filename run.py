import os
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Run the SRE Coworker Streamlit app with custom options.")
    parser.add_argument('--port', type=int, default=8080, help='Port to run the server on')
    parser.add_argument('--base_url_path', default='sreCowork', help='Base URL path for the app')
    parser.add_argument('--host', default='localhost', help='Host to bind the server to')

    args = parser.parse_args()

    # Set environment variables for Streamlit
    os.environ['STREAMLIT_SERVER_PORT'] = str(args.port)
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_BASE_URL_PATH'] = args.base_url_path
    os.environ['STREAMLIT_SERVER_ADDRESS'] = args.host

    # Run the Streamlit app
    subprocess.run(['streamlit', 'run', 'app.py'])

if __name__ == "__main__":
    main()