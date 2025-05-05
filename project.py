class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, Hours):
        if Hours == 7:
            self.mood = "happy"
        elif Hours < 7:
            self.mood = "tired"
        else:
           self.mood =  "Lazy"
        
    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            raise ValueError("Please Calculate Your Meals !")

    def buy(self, items):
        self.money -= (items*10)
        return 

class Employee(Person):
    def __init__(self,name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id 
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        print(f"{self.name} is driving {distance} km at {self.car.velocity} km/h.")
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount = 100):
        self.car.fuelRate += gasAmount

    def send_mail(self):
        pass

class Office:
    Employee_num = 0
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees if employees else []

    def get_all_employee(self):
       return self.employees

    def get_employee(self, emId):
        for emp in self.employees:
            if emId == emp.id:
                return emp
        return None
        
    def hire(self,employee):
        self.employees.append(employee)
        Office.Employee_num += 1
        print(f'Hired {employee.name}')
        
    def fire(self, emId):
        emp = self.get_employee(emId)
        if emp:
            self.employees.remove(emp)
            print(f"fired {emp.name}")
        else:
            print("Employee Not Found !")
        
    def deduct(self,empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} from {emp.name} salary's and it's new salary is {emp.salary} ")
        else:
            print("Employee Not Found !")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"Employee with name {emp.name} has been rewarded by {reward} and it's new salary is {emp.salary}")
        else:
            print("Employee Not Found !")
    
    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity + 1)
            if is_late:
                self.deduct(empId, 10)
                print(f"{emp.name} is late.")
            else:
                self.reward(empId, 10)
                print(f"{emp.name} is on time.")
        else:
                print("Employee not found.")
        
    @staticmethod
    def calculate_lateness(targetHour , moveHour, distance, velocity ):
        if velocity <= 0:
            print("Invalid velocity: must be greater than 0 to calculate travel time.")
            return True
        travel_time =( distance / velocity ) 
        arrival_time = (moveHour + travel_time) % 24  
        print(arrival_time)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.Employee_num = num 
            
        

class car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = min(max(fuelRate, 0), 100)
        self._velocity = min(max(velocity, 0), 200)

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = min(max(value, 0), 100)

    @property
    def velocity(self):
        return self._velocity
        
    @velocity.setter
    def velocity(self, value):
        self._velocity = min(max(value, 0), 200)

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = distance * 0.1
        if self.fuelRate >= fuel_needed:
            self.fuelRate = self.fuelRate - fuel_needed
            self.stop(0)
        else:
            max_distance = self.fuelRate * 10
            remain_distance = distance - max_distance
            self.fuelRate = 0
            self.stop(remain_distance)

    def stop(self, rem_distance):
        
        if rem_distance == 0:
            print("you arrive to your distnation")
            self.velocity = 0
            
        else:
            print(f"Remaining distance: {rem_distance} km.")




car1 = car(name="Fiat_128", fuelRate=40, velocity=100)


emp1 = Employee(
    name="Samy",
    money=1000,
    mood="neutral",
    healthRate=80,
    id=1,
    car=car1,
    email="samy@example.com",
    salary=5000,
    distanceToWork=50
)


office = Office(name="ITI", employees=[])
office.hire(emp1)

# Test employee actions
emp1.sleep(6)
emp1.eat(2)
emp1.buy(3)
emp1.work(9)
emp1.drive(50)
emp1.refuel(40)


# Test office actions
office.check_lateness(empId=1, moveHour=8)
office.fire(1)

print(f"\nFinal Status of {emp1.name}:")
print(f"Money: {emp1.money}")
print(f"Mood: {emp1.mood}")
print(f"Health: {emp1.healthRate}")
print(f"Salary: {emp1.salary}")
print(f"Fuel Rate: {emp1.car.fuelRate}")
