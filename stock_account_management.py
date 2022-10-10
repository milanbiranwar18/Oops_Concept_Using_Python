class Stock_Fun():
    def __init__(self, stock_dict):
        self.share_name = stock_dict.get("share_name")
        self.number_of_share = stock_dict.get("number_of_share")
        self.share_price = stock_dict.get("share_price")

    def stock_function(self):
        print("Company Name is", self.share_name)
        print("Number of share is", self.number_of_share)
        print("Price of one share is", self.share_price)
        print("Total Price of shares is", self.number_of_share*self.share_price)


if __name__ == '__main__':
    stock_list = [
        {
            "share_name": "Parle",
            "number_of_share": 123,
            "share_price": 500
        },
        {
            "share_name": "Reliance",
            "number_of_share": 186,
            "share_price": 600
        },
        {
            "name": "Google",
            "number_of_share": 165,
            "share_price": 800
        }
    ]

    for i in range(len(stock_list)):
        person = Stock_Fun(stock_list[i])
        print(person.stock_function())