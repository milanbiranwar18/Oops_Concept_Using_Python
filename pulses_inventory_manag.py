class Pulses_Fun():

    def __init__(self, pulses_dict):
        self.name_of_pulses = pulses_dict.get("name")
        self.weight_of_pulses = pulses_dict.get("weight")
        self.price_of_pulses = pulses_dict.get("price")

    def pulses_function(self):
        print("Pulses Name is", self.name_of_pulses)
        print("Weight of Pulses is", self.weight_of_pulses)
        print("Price of Pulses per KG", self.price_of_pulses)
        print("Total Price of Pulses", self.weight_of_pulses*self.price_of_pulses)


if __name__ == '__main__':
    pulses_list = [
        {
            "name": "green gram",
            "weight": 10,
            "price": 70
        },
        {
            "name": "kidney beans",
            "weight": 10,
            "price": 90
        },
        {
            "name": "split red lentils",
            "weight": 10,
            "price": 160
        },
        {
            "name": "yellow pigeon peas",
            "weight": 10,
            "price": 80
        }
    ]

    for i in range(len(pulses_list)):
        person = Pulses_Fun(pulses_list[i])
        print(person.pulses_function())