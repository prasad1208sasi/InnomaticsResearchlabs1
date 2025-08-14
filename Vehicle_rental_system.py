class Vehicle:
    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, is_available):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.rental_rate_per_day = rental_rate_per_day
        self.is_available = is_available
        self.number_of_days = 0

    def display_info(self):
        print('-------------------------------------------------------------------')
        print(f'Vehicle ID: {self.vehicle_id}\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\n'
              f'Rent/Day: {self.rental_rate_per_day}\nAvailable: {self.is_available}')

    def rent_vehicle(self, days=1):
        print('-------------------------------------------------------------------')
        if self.is_available:
            self.is_available = False
            self.number_of_days = days
            print(f"Vehicle {self.vehicle_id} rented successfully for {days} days!")
        else:
            print(f"Vehicle {self.vehicle_id} is already rented!")

    def return_vehicle(self):
        print('-------------------------------------------------------------------')
        if not self.is_available:
            self.is_available = True
            self.number_of_days = 0
            print(f"Vehicle {self.vehicle_id} returned successfully!")
        else:
            print(f"Vehicle {self.vehicle_id} was not rented!")

    @property
    def rental_cost(self):
        return self.rental_rate_per_day * self.number_of_days


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, is_available, seats, fuel_type):
        super().__init__(vehicle_id, brand, model, year, rental_rate_per_day, is_available)
        self.seats = seats
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Seats: {self.seats}, Fuel Type: {self.fuel_type}")


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, rental_rate_per_day, is_available, cc, helmet_required):
        super().__init__(vehicle_id, brand, model, year, rental_rate_per_day, is_available)
        self.cc = cc
        self.helmet_required = helmet_required

    def display_info(self):
        super().display_info()
        print(f"CC: {self.cc}, Helmet Required: {self.helmet_required}")


class Customer:
    total_rented_count = 0

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.__email = email
        self.rented_vehicles = []

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email
            print(f"Email updated to: {self.__email}")
        else:
            print("Invalid email format.")

    def rent(self, vehicle, days=1):
        if vehicle.is_available:
            self.rented_vehicles.append(vehicle)
            vehicle.rent_vehicle(days)
            Customer.total_rented_count += 1
            print(f"{self.name} rented {vehicle.brand} {vehicle.model} for {days} days. Estimated Cost: ${vehicle.rental_cost}")
        else:
            print(f"Sorry {self.name}, {vehicle.brand} {vehicle.model} is not available.")

    def return_vehicle(self, vehicle_id):
        for vehicle in self.rented_vehicles:
            if vehicle.vehicle_id == vehicle_id:
                vehicle.return_vehicle()
                self.rented_vehicles.remove(vehicle)
                print(f"{self.name} returned {vehicle.brand} {vehicle.model}.")
                return
        print(f"{self.name} does not have a vehicle with ID {vehicle_id} rented.")

    def display_rented_vehicles(self):
        if not self.rented_vehicles:
            print(f"{self.name} has no rented vehicles.")
        else:
            print(f"{self.name}'s Rented Vehicles:")
            for vehicle in self.rented_vehicles:
                vehicle.display_info()

    @classmethod
    def get_total_rented(cls):
        return cls.total_rented_count


class RentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_customer(self, customer):
        self.customers.append(customer)

    def search_available_vehicles(self):
        print("\nAvailable Vehicles:")
        found = False
        for vehicle in self.vehicles:
            if vehicle.is_available:
                vehicle.display_info()
                found = True
        if not found:
            print("No vehicles available.")

    def show_all_rented_vehicles(self):
        print("\nAll Rented Vehicles:")
        found = False
        for vehicle in self.vehicles:
            if not vehicle.is_available:
                vehicle.display_info()
                found = True
        if not found:
            print("No vehicles are currently rented.")


# ---------------- Example Usage ----------------
system = RentalSystem()

car1 = Car("C101", "Toyota", "Camry", 2022, 70, True, 5, "Petrol")
bike1 = Bike("B201", "Honda", "Shine", 2023, 30, True, "125cc", True)

system.add_vehicle(car1)
system.add_vehicle(bike1)

customer1 = Customer(1, "Alice", "alice@example.com")
system.add_customer(customer1)

system.search_available_vehicles()

customer1.rent(car1, 3)
customer1.display_rented_vehicles()

system.show_all_rented_vehicles()

customer1.return_vehicle("C101")
system.search_available_vehicles()

print("\nTotal vehicles rented so far:", Customer.get_total_rented())
