from flask_restful import Resource, reqparse
from  api.models.task import Task
from api import mlab

class TaskListRes(Resource) :
    def get(self):
        tasks = Task.objects()
        tasks_json = mlab.list2json(tasks)
        return tasks_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name",type=str, location="json")
        parser.add_argument(name="local_id",type=str, location="json")
        parser.add_argument(name="done",type=bool, location="json")

        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        task = Task(name=name,local_id=local_id,done =False)
        task.save()

        added_task = Task.objects().with_id(task.id)
        return mlab.item2json(added_task)