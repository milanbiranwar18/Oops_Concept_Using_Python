class Wheats_Fun():
    def __init__(self, wheats_dict):
        self.name_of_wheat = wheats_dict.get("name")
        self.weight_of_wheat = wheats_dict.get("weight")
        self.price_of_wheat = wheats_dict.get("price")

    def wheat_function(self):
        print("Wheat Name is", self.name_of_wheat)
        print("Weight of wheat is", self.weight_of_wheat)
        print("Price of wheat per KG", self.price_of_wheat)
        print("Total Price of wheat", self.weight_of_wheat*self.price_of_wheat)


if __name__ == '__main__':
    wheat_list = [
        {
            "name": "Triticum vulgare",
            "weight": 10,
            "price": 45
        },
        {
            "name": "durum",
            "weight": 10,
            "price": 35
        },
        {
            "name": "compactum",
            "weight": 10,
            "price": 40
        }
    ]

    for i in range(len(wheat_list)):
        person = Wheats_Fun(wheat_list[i])
        print(person.wheat_function())