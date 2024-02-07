from string import Template


class myTemplate(Template):
    delimiter = "#"


def main():
    cart = []
    cart.append(dict(item="cake", price=85, quantity=6))
    cart.append(dict(item="key", price=62, quantity=8))
    cart.append(dict(item="fish", price=104, quantity=9))
    '''
    cart = [{item: "cake", price: 85, quantity: 6},
    {item: "key", price: 62, quantity: 8},
    {item: "fish", price: 104, quantity: 9}
    ]
    '''

    t = myTemplate("#quantity x #item = #price")
    total = 0
    print("cart :")
    for data in cart:
        print(t.substitute(data))
        total += data["price"]
    print("total: "+str(total))


if __name__ == "__main__":
    main()
