class Person:
    def __init__(self, name):
        self.name = name
        self.expense = 0

    def add_expense(self, expense):
        self.expense += expense

    def current_expense(self):
        return self.expense


class Event:
    def __init__(self, title, attendees):
        self.title = title
        self.attendees = attendees
        self.price = 0

    def add_purchase(self, item, price, person):
        if person not in self.attendees:
            return "Not in attendees"
        person.add_expense(price)
        self.item = item
        self.price += price

    def total_price(self):
        return (self.price, round(self.price / len(self.attendees), 2))

    def price_per_attendee(self):
        total, price_for_each = self.total_price()
        print("total price was", total)
        print("price for each is", price_for_each)
        price_per_attendee = list(
            map(
                lambda person: {
                    "name": person.name,
                    "amount_owed": round(person.expense - price_for_each, 2),
                    "total": total,
                },
                self.attendees,
            )
        )
        positive_attendees = list(
            filter(lambda attendee: attendee["amount_owed"] > 0, price_per_attendee)
        )
        self.__calculate_expenses(positive_attendees, price_per_attendee)

    def __calculate_expenses(self, positive_attendees, price_per_attendee):
        for positive_attendee in positive_attendees:
            for person in price_per_attendee:
                print(person["name"], "has balance", "€" + str(person["amount_owed"]))
                if (
                    person["amount_owed"] < 0
                    and positive_attendee["name"] != person["name"]
                ):
                    print(
                        person["name"],
                        "pays",
                        positive_attendee["name"],
                        "€" + str(person["amount_owed"]),
                    )
                    positive_attendee["amount_owed"] += person["amount_owed"]
                    person["amount_owed"] -= person["amount_owed"]
        for person in price_per_attendee:
            print(person["name"], "has balance", "€" + str(person["amount_owed"]))
