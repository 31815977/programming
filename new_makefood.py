#new_makefood.py
def make_icecream(*toppings):
    """列出製作冰淇淋的配料"""
    print("這個冰淇淋所加配料如下")
    for topping in toppings:
        print("---",topping)
def make_drink(size,drink):
    print("所點飲料如下")
    print("---",size.title())
    print("---",drink.title())
def main():
    make_icecream('草莓醬')
    make_icecream('草莓醬', '葡萄乾', '巧克力碎片')
    make_drink('large', 'coke')
if __name__=="__main__":
    main()
