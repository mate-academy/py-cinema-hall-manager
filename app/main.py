from models import ActrModel
from managers import ActorFormatManagers


if __name__ == "__main__":
    ActrModel.objects = ActorFormatManagers()
    ActrModel.objects.create("Tom", "Backer")
    ActrModel.objects.create("Sam", "Cooker")
    print(ActrModel.objects.all())
    ActrModel.objects.update(2, "Alfred", "Goos")
    print(ActrModel.objects.all())
    ActrModel.objects.delete(1)
    print(ActrModel.objects.all())
