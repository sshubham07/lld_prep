from LockerPackage import LockerPackage
from Locker import Locker
from Notification import Notification

class DeliveryPerson:
    def __init__(self, delivery_person_id: str):
        self.delivery_person_id = delivery_person_id

    def deliver_package(self, pkg: LockerPackage, locker: Locker):
        if locker.add_package(pkg):
            print(f"DeliveryPerson {self.delivery_person_id} delivered package {pkg.package_id} to locker {locker.locker_id}")

    def pickup_return(self, pkg: LockerPackage, locker: Locker):
        if locker.remove_package(pkg.code):
            print(f"DeliveryPerson {self.delivery_person_id} picked up returned package {pkg.package_id} from locker {locker.locker_id}")

    def receive_return_notification(self, notification: Notification):
        print(f"DeliveryPerson {self.delivery_person_id} received return notification for locker {notification.locker_id}")
