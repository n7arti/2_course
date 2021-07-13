import Project


class NegValException(Exception):
    pass


def main():
    Project.Product.name = input("Введите название товара: ")
    while 1:
        try:
            Project.Product.pricerub = int(input("Введите цену товара в рублях: "))
            if Project.Product.pricerub <= 0:
                raise NegValException("Цена должна быть больше 0.")
        except ValueError:
            print("Введены некорректные данные. Введите число.")
        except NegValException as e:
            print(e)
        else:
            break
    Project.Product.manfac = input("Введите производителя: ")
    product1 = Project.Product(Project.Product.name, Project.Product.pricerub, Project.Product.manfac)
    with open("DataBase.txt", "wb") as file:
        mas = [product1.name, product1.pricerub, product1.manfac]
        for i in mas:
            line = str(i) + '\n'
            file.write(line.encode())
    file.close()

    with open("DataBase.txt", "rb") as file:
        try:
            product = Project.Product()
            contents = file.readlines()
            size = len(contents)
            for i in range(0, size, 3):
                product.name = contents[i].decode().rstrip('\n')
                product.pricerub = int(contents[i + 1].decode())
                if product.pricerub <= 0:
                    raise NegValException("Цена должна быть больше 0.")
                product.manfac = contents[i + 2].decode().rstrip('\n')
        except ValueError:
            print("Введены некорректные данные. Введите число.")
        except NegValException as e:
            print(e)
    print(product)


if __name__ == "__main__":
    main()
