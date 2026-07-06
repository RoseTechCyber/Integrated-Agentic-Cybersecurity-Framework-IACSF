from azure.cosmos import ContainerProxy

class Control:
    def __init__(self, id: str, title: str, active: bool):
        self.id = id
        self.title = title
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "active": self.active
        }

def create_control(container: ContainerProxy, control: Control):
    try:
        container.create_item(body=control.to_dict())
        print("Created control:", control.to_dict())
    except Exception as e:
        print("Error creating control id", e)
        raise e

def read_control(container: ContainerProxy, control_id: str) -> Control:
    try:
        item_response = container.read_item(item=user_id, partition_key=control_id)
        return Control(item_response["id"], item_response["title"], item_response["active"])
    except Exception as e:
        print("Error reading control info", e)
        raise e
