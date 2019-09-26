from subprocess import call

if __name__ == "__main__":
    a = call('gunicorn -c c.py run:app', shell=True)
    print(a)