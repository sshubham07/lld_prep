from datetime import datetime
from LockerService import LockerService
from LockerLocation import LockerLocation
from Locker import Locker
from LockerSize import LockerSize
from Customer import Customer
from DeliveryPerson import DeliveryPerson
from Order import Order
from Item import Item
from Package import Package
from LockerPackage import LockerPackage
from Notification import Notification

def separator(char='=', length=100):
    return char * length

def main():
    print(separator())
    print("\t\t\t\t\tAMAZON LOCKER SERVICE SYSTEM")
    print(separator())

    print("🛠️  [SETUP] Initializing Locker Service, Locations, and Lockers...\n")
    locker_service = LockerService.get_instance()

    now = datetime.now()
    loc = LockerLocation("Downtown", 10.5, 20.8, now, now)
    locker1 = Locker("L1", LockerSize.MEDIUM, loc.name)
    locker2 = Locker("L2", LockerSize.LARGE, loc.name)
    loc.add_locker(locker1)
    loc.add_locker(locker2)
    locker_service.add_location(loc)

    print("    → Added LockerLocation: Downtown with Lockers: [L1, L2]\n")

    customer = Customer("CUST1", "Alice", "alice@example.com", "1234567890")
    delivery_guy = DeliveryPerson("DEL1")

    print("1️⃣  SCENARIO 1: Customer Places an Order")
    print(separator('-'))
    order = Order("ORD1", loc.name, customer.customer_id)
    order.add_item(Item("ITM1", 2))
    print("  → [Customer] Placing order ORD1 for 2x ITM1.")
    customer.place_order(order)

    pkg = Package("PKG1", 2.5, order)
    print("  → [System] Packing the order...")
    pkg.pack()

    print("  → [System] Assigning a locker for package delivery...")
    assigned_locker = locker_service.request_locker(LockerSize.MEDIUM)
    otp = "123456"
    lpkg = LockerPackage("PKG1", 2.5, order, 3, assigned_locker.locker_id, otp, datetime.now(), delivery_guy.delivery_person_id)

    print("  → [DeliveryPerson] Delivering package PKG1 to Locker L1...")
    delivery_guy.deliver_package(lpkg, assigned_locker)

    notification = Notification(customer.customer_id, order.order_id, assigned_locker.locker_id, otp)
    print("  → [System] Sending pickup notification to customer...")
    notification.send()
    customer.receive_notification(notification)

    print("\n2️⃣  SCENARIO 2: Customer Picks Up the Package")
    print(separator('-'))
    print("  → [Customer] Arriving at Locker L1 to pick up package.")
    if assigned_locker.remove_package(otp):
        print("    ✔️  [Customer] Pickup successful! Package retrieved from locker L1.")
    else:
        print("    ❌ [Customer] Pickup failed.")

    print("\n3️⃣  SCENARIO 3: Customer Initiates a Return")
    print(separator('-'))
    customer.request_return(order)
    if locker_service.request_return(order):
        print("  → [System] Return approved! Assigning locker for return...")
        return_locker = locker_service.request_locker(LockerSize.MEDIUM)
        return_otp = "654321"
        return_pkg = LockerPackage("PKG1-R", 2.5, order, 3, return_locker.locker_id, return_otp, datetime.now(), delivery_guy.delivery_person_id)

        return_notif = Notification(customer.customer_id, order.order_id, return_locker.locker_id, return_otp)
        print("  → [System] Sending return locker details to customer...")
        return_notif.send()
        customer.receive_notification(return_notif)

        print("  → [System] Notifying DeliveryPerson about expected return...")
        delivery_guy.receive_return_notification(return_notif)

        print(f"  → [Customer] Placing return package PKG1-R in Locker {return_locker.locker_id}...")
        return_locker.add_package(return_pkg)
        print(f"      ↳ [Customer] Return package placed in locker {return_locker.locker_id}.")

        print("  → [DeliveryPerson] Arriving to pick up returned package...")
        delivery_guy.pickup_return(return_pkg, return_locker)

    print("\n🏁\t\t\t\t\tSYSTEM DEMO COMPLETE")
    print(separator())

if __name__ == "__main__":
    main()
