#NAME: Arpita Mishra
#Enrollment Number: E22CSEU0988
class Flight:
    def __init__(self, flight_id, source_city, destination_city, price):
        self.flight_id = flight_id
        self.source_city = source_city
        self.destination_city = destination_city
        self.price = price
class FlightDatabase:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)
    2

    def search_by_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source_city):
        result = []
        for flight in self.flights:
            if flight.source_city == source_city:
                result.append(flight)
        return result

    def search_by_destination(self, destination_city):
        result = []
        for flight in self.flights:
            if flight.destination_city == destination_city:
                result.append(flight)
        return result

def main():
    database = FlightDatabase()

    database.add_flight(Flight("AI161E90", "BLR", "BOM",5600 ))
    database.add_flight(Flight("BR161F91", "BOM", "BBI",6750 ))
    database.add_flight(Flight("AI161F99","BBI","BLR",8210))
    database.add_flight(Flight("VS171E20","JLR","BBI",5500))
    database.add_flight(Flight("AS171G30","HYD","JLR",4400))
    database.add_flight(Flight("AI131F49","HYD","BOM",3499))
    

    user_input = int(input("Enter 1 to search by Flight ID, 2 for source city, or 3 for destination city: "))

    if user_input == 1:
        flight_id = input("Enter Flight ID: ")
        flight = database.search_by_id(flight_id)
        if flight:
            print("Flight ID:", flight.flight_id)
            print("Source City:", flight.source_city)
            print("Destination City:", flight.destination_city)
            print("Price:", flight.price)
        else:
            print("Flight not found.")

    elif user_input == 2:
        source_city = input("Enter Source City: ")
        flights = database.search_by_source(source_city)
        if flights:
            for flight in flights:
                print("Flight ID:", flight.flight_id)
                print("Source City:", flight.source_city)
                print("Destination City:", flight.destination_city)
                print("Price:", flight.price)
        else:
            print("No flights found from the given source city.")

    elif user_input == 3:
        destination_city = input("Enter Destination City: ")
        flights = database.search_by_destination(destination_city)
        if flights:
            for flight in flights:
                print("Flight ID:", flight.flight_id)
                print("Source City:", flight.source_city)
                print("Destination City:", flight.destination_city)
                print("Price:", flight.price)
        else:
            print("No flights found to the given destination city.")

    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()