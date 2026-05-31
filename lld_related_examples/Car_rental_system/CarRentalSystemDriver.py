from datetime import datetime, timedelta

from CarRentalSystem import CarRentalSystem
from CarRentalBranch import CarRentalBranch
from Address import Address
from Car import Car
from Van import Van
from CarType import CarType
from VanType import VanType
from VehicleStatus import VehicleStatus
from VehicleCatalog import VehicleCatalog
from Customer import Customer
from AccountStatus import AccountStatus
from VehicleReservation import VehicleReservation
from ReservationStatus import ReservationStatus
from ChildSeat import ChildSeat
from DriverService import DriverService
from CreditCard import CreditCard
from PaymentStatus import PaymentStatus
from EmailNotification import EmailNotification
from SmsNotification import SmsNotification
from Fine import Fine

def main():
    print("=============================================")
    print("        CAR RENTAL SYSTEM DEMO")
    print("=============================================\n")

    # 1. Branch Setup
    print("1. Branch Setup")
    rental_system = CarRentalSystem.get_instance()
    branch1 = CarRentalBranch(
        "Airport Branch",
        Address("123 Main St", "Seattle", "WA", 98101, "USA"),
        []
    )
    rental_system.add_new_branch(branch1)
    print(f"   -> Branch added: {branch1.get_name()} ({branch1.get_location()})\n")

    # 2. Add Vehicles
    print("2. Adding Vehicles to Inventory")
    car1 = Car()
    car1.set_vehicle_id("C1001")
    car1.set_model("Toyota Corolla")
    car1.set_manufacturing_year(2022)
    car1.set_car_type(CarType.ECONOMY)
    car1.set_status(VehicleStatus.AVAILABLE)

    van1 = Van()
    van1.set_vehicle_id("V1001")
    van1.set_model("Ford Transit")
    van1.set_manufacturing_year(2021)
    van1.set_van_type(VanType.PASSENGER)
    van1.set_status(VehicleStatus.AVAILABLE)

    catalog = VehicleCatalog()
    catalog.add_vehicle(car1)
    catalog.add_vehicle(van1)

    print("   -> Vehicles added: ")
    print(f"      - {car1.get_model()} (ID: {car1.get_vehicle_id()})")
    print(f"      - {van1.get_model()} (ID: {van1.get_vehicle_id()})\n")

    # 3. Customer Registration
    print("3. Customer Registration & Login")
    customer1 = Customer()
    customer1.set_account_id("U123")
    customer1.set_name("Alice Smith")
    customer1.set_email("alice@email.com")
    customer1.set_license_number("D1234567")
    customer1.set_license_expiry(datetime(2027, 2, 1))
    customer1.set_status(AccountStatus.ACTIVE)

    print(f"   -> [LOGIN] Customer: {customer1.get_name()} (ID: {customer1.get_account_id()})")
    print(f"   -> Driver License #: {customer1.get_license_number()} (Expires: {customer1.get_license_expiry()})\n")

    # 4. Vehicle Search by Customer
    print("4. Vehicle Search")
    print("   == Vehicle Inventory Search Results ==")
    cars = catalog.search_by_type("CAR")
    if cars:
        print(f"   -> Found {len(cars)} car(s) in inventory:")
        for v in cars:
            print(f"      -> Model: {v.get_model()} | ID: {v.get_vehicle_id()} | Year: {v.get_manufacturing_year()} | Status: {v.get_status()}")
    else:
        print("   -> No cars found in inventory.")
    print()

    # 5. Make a Reservation
    print("5. Reservation")
    reservation = VehicleReservation()
    reservation.set_reservation_id(1)
    reservation.set_customer_id(customer1.get_account_id())
    reservation.set_vehicle_id(car1.get_vehicle_id())
    reservation.set_creation_date(datetime.now())
    reservation.set_status(ReservationStatus.PENDING)
    reservation.set_pickup_location("Airport Branch")
    reservation.set_return_location("Airport Branch")
    reservation.set_due_date(datetime.now() + timedelta(days=3))

    all_reservations = [reservation]

    car1.reserve_vehicle()
    print(f"   -> Reservation created for {customer1.get_name()} | Vehicle: {car1.get_model()} | Pickup: {reservation.get_pickup_location()} | Return: {reservation.get_return_location()} | Due: {reservation.get_due_date()}")

    # 6. Add Equipment and Services
    print("\n6. Add-ons: Equipment & Services")
    seat = ChildSeat()
    seat.set_equipment_id(10)
    seat.set_price(15)
    reservation.add_equipment(seat)

    driver_service = DriverService()
    driver_service.set_service_id(20)
    driver_service.set_price(50)
    driver_service.set_driver_id(222)
    reservation.add_service(driver_service)

    print(f"   -> Equipment added: Child Seat (ID: {seat.get_equipment_id()}, Price: ${seat.get_price()})")
    print(f"   -> Service added: Driver (Driver ID: {driver_service.get_driver_id()}, Price: ${driver_service.get_price()})\n")

    # 7. Payment Processing
    print("7. Payment Processing")
    reservation.set_status(ReservationStatus.CONFIRMED)
    payment = CreditCard()
    payment.set_amount(200)
    payment.set_timestamp(datetime.now())
    payment.set_status(PaymentStatus.PENDING)
    print(f"   -> Processing payment of ${payment.get_amount()} ...")
    payment_success = payment.make_payment()

    if payment_success:
        print(f"   -> Payment completed successfully for reservation #{reservation.get_reservation_id()}")
    else:
        print("   -> Payment failed!")
    print()

    # 8. Notification (Email)
    print("8. Notification")
    notify = EmailNotification()
    notify.set_content("Your reservation is confirmed!")
    notify.send_notification(customer1)
    print()

    # 9. Vehicle Pickup
    print("9. Vehicle Pickup")
    print(f"   -> {customer1.get_name()} picked up the vehicle: {car1.get_model()} ({car1.get_vehicle_id()})\n")

    # 10. Vehicle Return
    print("10. Vehicle Return")
    return_date = datetime.now() + timedelta(days=3)  # Returned on due date
    car1.return_vehicle()
    reservation.set_return_date(return_date)
    reservation.set_status(ReservationStatus.COMPLETED)

    print(f"   -> Vehicle returned on: {reservation.get_return_date()}")
    print(f"   -> Reservation status is now: {reservation.get_status()}\n")

    # 11. Overdue Fine Check
    print("11. Fine Calculation")
    expected_return = reservation.get_due_date()
    actual_return = reservation.get_return_date()
    if actual_return > expected_return:
        fine = Fine()
        fine.set_amount(100)
        fine.set_reason("Late return")
        print(f"   -> [FINE] Fine imposed for late return: ${fine.get_amount()}")
        fine_notify = SmsNotification()
        fine_notify.set_content("You have been fined for late return.")
        fine_notify.send_notification(customer1)
    else:
        print("   -> [FINE] No fine. Vehicle was returned on time.")
    print()

    # 12. Reservation History for Customer
    print(f"12. Reservation History for Customer: {customer1.get_name()}")
    print("   -------------------------------------")
    for r in all_reservations:
        if r.get_customer_id() == customer1.get_account_id():
            print(f"   -> Reservation ID: {r.get_reservation_id()} | Vehicle: {r.get_vehicle_id()} | Status: {r.get_status()} | Pickup: {r.get_pickup_location()} | Returned: {r.get_return_date()}")
    print("=============================================")
    print("             END OF DEMO")
    print("=============================================")

if __name__ == "__main__":
    main()