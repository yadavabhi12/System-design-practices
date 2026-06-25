from abc import ABC, abstractmethod


class OfficeMachine(ABC):
    """
    BAD DESIGN

    Every machine is forced to implement
    all methods even when it doesn't need them.
    """

    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def fax_document(self):
        pass

    @abstractmethod
    def email_document(self):
        pass











# Simple Printer


class BasicPrinter(OfficeMachine):

    def print_document(self):
        print("Printing document...")

    def scan_document(self):
        # Printer cannot scan
        raise NotImplementedError(
            "Basic printer does not support scanning"
        )

    def fax_document(self):
        # Printer cannot fax
        raise NotImplementedError(
            "Basic printer does not support fax"
        )

    def email_document(self):
        # Printer cannot email
        raise NotImplementedError(
            "Basic printer does not support email"
        )
    





# Scanner

class ScannerDevice(OfficeMachine):

    def print_document(self):
        raise NotImplementedError(
            "Scanner cannot print"
        )

    def scan_document(self):
        print("Scanning document...")

    def fax_document(self):
        raise NotImplementedError(
            "Scanner cannot fax"
        )

    def email_document(self):
        raise NotImplementedError(
            "Scanner cannot email"
        )





# PROBLEM 1
# Classes implement methods they don't need

# PROBLEM 2
# Many NotImplementedError methods

# PROBLEM 3
# Hard maintenance

# PROBLEM 4
# If new method added,
# every class must change

# PROBLEM 5
# Violates Interface Segregation Principle