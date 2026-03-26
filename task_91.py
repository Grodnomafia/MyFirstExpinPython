from dataclasses import dataclass

@dataclass
class Item:
    name : str
    price: float
    qty : int = 1

    def total_sum(self)->float:
        return self.price * self.qty


@dataclass
class PercentDiscount:
    percent_num :int

    def percent(self,total) -> float:
        return total * (self.percent_num /100)


class NonDiscount:
    def percent(self,total)->int:
        return 0


class Order:
    def __init__(self,item: list[Item],policy):
       self.item = item
       self.policy = policy


    def total(self)->float:
        return  sum(i.total_sum() for i in self.item)

    def set_policy(self,policy):
        self.policy = policy

    def total_with_discount(self):
        t = self.total()
        return t - self.policy.percent(t)

basket = [Item('Ершик',200,3),Item('Бумага',100,5)]
order = Order(basket, NonDiscount())
print(order.total())
print(order.total_with_discount())
order.set_policy(PercentDiscount(10))
print(order.total())
print(order.total_with_discount())