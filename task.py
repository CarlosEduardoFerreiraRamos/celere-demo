from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379/0')

@app.task(bind=True)
def add(self,x, y):
    val = x + y
    # self.update_state(state='STARTED', meta={'value':'Loaded'})
    val = val + val
    return val
