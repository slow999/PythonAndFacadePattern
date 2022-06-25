from __future__ import annotations
import datetime


class CheckoutFacade:
    def __init__(self, inventory_system: InventorySystem = None, shipping_system: ShippingSystem = None,
                 billing_system: BillingSystem = None) -> None:
        self._inventory_system = inventory_system or InventorySystem()
        self._shipping_system = shipping_system or ShippingSystem()
        self._billing_system = billing_system or BillingSystem()

    def submit_order(self, items: list) -> str:
        result = []
        result.append(self._inventory_system.order_item())
        result.append(self._billing_system.validate_credit_card())
        result.append(self._billing_system.post_transaction())
        result.append(self._shipping_system.print_shipping_label())
        return '\n'.join(result)


class BillingSystem:
    def post_transaction(self):
        return "Your credit card is charged"

    # ...

    def validate_credit_card(self):
        return "Your credit card is validated"


class InventorySystem:
    def check_item_promotion(self):
        return True

    # ...

    def order_item(self):
        return "{'id': 2, 'name': 'keyboard', 'quantity': 2}"

    def revert_item(self):
        return "Your ordered items have been reverted."

    def cal_num_of_boxes(self):
        return "Need 2 boxes to package all items."


class ShippingSystem:
    def list_service_and_rate(self, ship_date: datetime.date, weight: int):
        ship_date = ship_date or datetime.datetime.today()
        return ['FO', 'SO', 'FG', 'XS']

    # ...

    def can_deliver(self, **kwargs):
        return True

    def print_shipping_label(self):
        return "label.pdf"


def client_code(facade: CheckoutFacade) -> None:
    items = [
        {'id': 1, 'name': 'keyboard', 'quantity': 1},
        {'id': 5, 'name': 'monitor', 'quantity': 2},
        {'id': 12, 'name': 'usb cables', 'quantity': 7}
    ]
    result = facade.submit_order(items)
    print(result)


if __name__ == '__main__':
    shipping_system = ShippingSystem()
    billing_system = BillingSystem()
    facade = CheckoutFacade(shipping_system=shipping_system, billing_system=billing_system)
    client_code(facade=facade)
