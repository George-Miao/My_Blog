from main import app
import argparse


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', dest="database_switch")
    args = parser.parse_args()
    """
    app.run(host = "0.0.0.0", port=80, debug=True)

