# Singleton Pattern

## Problem

Suppose you are building a Logging System.

Initially every class creates its own Logger.

OrderService

↓

new Logger()

PaymentService

↓

new Logger()

UserService

↓

new Logger()

Every service creates a new Logger object.

Problems:

- High Memory Usage
- Multiple File Handles
- Duplicate Logs
- Configuration mismatch
- Difficult to maintain

Question:

Can we ensure only ONE Logger object exists in the entire application?

This is the exact problem Singleton Pattern solves.