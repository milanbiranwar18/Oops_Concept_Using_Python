class Rice_Fun():
    def __init__(self, rice_dict):
        self.name_of_rice = rice_dict.get("name")
        self.weight_of_rice = rice_dict.get("weight")
        self.price_of_rice = rice_dict.get("price")

    def rice_function(self):
        print("Rice Name is", self.name_of_rice)
        print("Weight of Rice is", self.weight_of_rice)
        print("Price of rice per KG", self.price_of_rice)
        print("Total Price of rice", self.weight_of_rice*self.price_of_rice)


if __name__ == '__main__':
    rice_list = [
        {
            "name": "Basumati",
            "weight": 10,
            "price": 50
        },
        {
            "name": "Ricel",
            "weight": 10,
            "price": 60
        },
        {
            "name": "DAAWAT",
            "weight": 10,
            "price": 80
        }
    ]

    for i in range(len(rice_list)):
        person = Rice_Fun(rice_list[i])
        print(person.rice_function())