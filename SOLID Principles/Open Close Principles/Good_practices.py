from abc import ABC ,abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")


class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

class UPIPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing UPI payment of ${amount:.2f}")




class PaymentGateway:
    def __init__(self, payment_method: PaymentProcessor):
        self.payment_method = payment_method

    def process_payment(self, amount: float):
        self.payment_method.process_payment(amount)




class main:
    if __name__ == "__main__":
        credit_card_processor = CreditCardPaymentProcessor()
        paypal_processor = PayPalPaymentProcessor()
        upi_processor = UPIPaymentProcessor()

        payment_processor = PaymentGateway(credit_card_processor)
        payment_processor.process_payment(100.0)

        payment_processor = PaymentGateway(paypal_processor)
        payment_processor.process_payment(500.0)

        
        payment_processor = PaymentGateway(upi_processor)
        payment_processor.process_payment(300.0)