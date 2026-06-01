class PaymentProcessor:
    def process_payment(self, amount: float, payment_type: str) -> None:
        if payment_type == "credit_card":
            print(f"Processing credit card payment of ${amount:.2f}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of ${amount:.2f}")
        elif payment_type == "upi":
            print(f"Processing UPI payment of ${amount:.2f}")
        else:
            print(f"Processing unknown payment type of ${amount:.2f}")

    def generate_report(self) -> None:
        print("Generating payment report...")


payment_processor = PaymentProcessor()
payment_processor.process_payment(100.0, "credit_card")
payment_processor.process_payment(200.0, "paypal")
payment_processor.process_payment(300.0, "upi")
payment_processor.process_payment(400.0, "bitcoin")