from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379/0')

@app.task(bind=True)
def add(self,x, y):
    val = x + y
    # self.update_state(state='STARTED', meta={'value':'Loaded'})
    val = val + val
    return val


"""
some devaniations about using celery 

OPTION ONE
    value_1 = *
    value_2 = **

    task = add.delay(value_1, value_2)

    id = task.id

    >> storage the #id
    them call the task again with the $id in "hands"

    id = storageId;

    task = add.AsyncResult(id);

    result = task.get()

OPTION TWO
    value_1 = *
    value_2 = **

    task = add.delay(value_1, value_2)

    while task.ready() not True:
        print(task.status)
    
    result = task.result // or task.get();

OPTION THREE
    >> store the request in a queue
    them the schedule will kick in processing the request

    value_1 = *
    value_2 = **

    task = add.delay(value_1, value_2)

    id = task.id

    >> storage the data updating the necessary info when needed
    whem finished

    id = storageId;

    task = add.AsyncResult(id);

    result = task.get()
"""