class Product:
    def __init__(self, name="Apelsin", pricerub=30, manfac="Ogorod"):
        self.__name = name
        while pricerub < 0:
            print("Не корректный ввод! Попробуйте снова.")
            pricerub = int(input())
        self.__pricerub = pricerub
        self.__manfac = manfac

    def __del__(self):
        print("Товар ", self.name, " удален из памяти")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def pricerub(self):
        return self.__pricerub

    @pricerub.setter
    def pricerub(self, pricerub):
        self.__pricerub = pricerub

    @property
    def manfac(self):
        return self.__manfac

    @manfac.setter
    def manfac(self, manfac):
        self.__manfac = manfac

    def euro(self):
        priceeuro = self.pricerub
        priceeuro *= 0.011
        return priceeuro

    def samsung(self):
        new_cost = self.euro()
        if self.__name == "Samsung":
            new_cost *= 2
        return new_cost

    def __str__(self):
        return "Наименование: {} \t Цена в рублях: {} \t Изготовитель: {}\n".format(self.name, self.pricerub,
                                                                                   self.manfac)


class AllInformation(Product):
    def __init__(self, name="Apelsin", pricerub=30, manfac="Ogorod", type="Fruit", regnumb=1):
        Product.__init__(self, name, pricerub, manfac)
        self.__type = type
        while regnumb < 0:
            print("Не корректный ввод! Попробуйте снова.")
            regnumb = int(input())
        self.__regnumb = regnumb

    def __del__(self):
        print("Товар ", self.name, " удален из памяти")

    @property
    def type(self):
        return self.__type

    @property
    def regnumb(self):
        return self.__regnumb



    def __str__(self):
        return "Наименование: {} \t Цена в рублях: {} \t Изготовитель:{} \t Тип: {} \t Регистрационный номер: {} \n".format(
            self.name, self.pricerub,
            self.manfac, self.type, self.regnumb)


class Booking(Product):
    def __init__(self, name="Apelsin", pricerub=30, manfac="Ogorod", count=2):
        Product.__init__(self, name, pricerub, manfac)
        self.__count = count

    def __del__(self):
        print("Товар ", self.name, " удален из памяти")

    @property
    def count(self):
        return self.__count

    def euro(self):
        priceeuro = self.pricerub * self.count
        priceeuro *= 0.011
        return priceeuro

    def __str__(self):
        return "Наименование: {} \t Цена в рублях: {} \t Изготовитель:{} \t Количество: {} \n".format(self.name,
                                                                                                      self.pricerub,
                                                                                                      self.manfac,
                                                                                                      self.count)
