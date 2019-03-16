from flask import Flask
from api import mlab
from api.models.task import Task
from flask_restful import *
from api.resources.task_resources import *


mlab.connect
app = Flask(__name__)
api = Api(app)
task = Task(name="Hiếu",local_id="1sadsad",done=False)
task.save()

api.add_resource(TaskListRes,"/task")

if __name__ == '__main__' :
    app.run()
