import requests
import subprocess
import sys
import time


def run_container(image):
    try:
        result = subprocess.run(f"IMAGE={image}docker-compose up -d --remove-orphans", shell=True, capture_output=True, text=True)
        print(f"Result subprocess {result}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running docker-compse command: {e}")
        return None


def test_container(endpoint_url,image):
    try:
        output = run_container(image)
        if output:
            time.sleep(5)
            response = requests.get(endpoint_url)

            if response.status_code == 200:
                print("Endpoint request was successful")
                return True
            else:
                print("Endpoint did not return status code od 200. Request failed")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Usage: python test-container.py image")
        sys.exit(1)
    
    endpoint_url = "localhost:35000/health"
    image = sys.argv[0]

    print(test_container(endpoint_url, image))