from multiprocessing import cpu_count

def max_workers():
    return cpu_count()

wsgi_app = "run:app"

bind = "0.0.0.0:5000"
workers = max_workers()