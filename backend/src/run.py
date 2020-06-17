from main import app


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', dest="database_switch")
    args = parser.parse_args()
    """
    app.config['COMPRESS_MIMETYPES'] = [
        'text/html',
        'text/css',
        'text/xml',
        'application/json',
        'application/javascript',
        'font/ttf',
        'font/otf'
    ]
    app.run(host="0.0.0.0", port=8888, debug=True)
