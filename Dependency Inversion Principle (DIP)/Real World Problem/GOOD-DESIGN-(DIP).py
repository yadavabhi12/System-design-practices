
"""
==========================================================
🚀 SOLID PRINCIPLE - D
🚀 Dependency Inversion Principle (DIP)
==========================================================

📌 Definition:

High-level modules should NOT depend on low-level modules.

Both should depend on abstractions.

In simple words:

❌ Bad:
Notification ---> EmailService

✅ Good:
Notification ---> MessageService (Interface)
                         ▲
                         │
        ┌────────────────┼───────────────┐
        │                │               │
        ▼                ▼               ▼
 EmailService      SMSService    WhatsAppService

----------------------------------------------------------
🎯 Problem DIP Solves
----------------------------------------------------------

Without DIP:

1️⃣ Tight Coupling
   Notification is directly connected to EmailService.

2️⃣ Difficult Maintenance
   If Email changes, Notification may change.

3️⃣ Difficult Testing
   Hard to create mock services.

4️⃣ Difficult Scaling
   Adding SMS or WhatsApp requires code modification.

5️⃣ Violates Open/Closed Principle
   Existing code must be modified.

----------------------------------------------------------
✅ With DIP
----------------------------------------------------------

1️⃣ Loose Coupling

2️⃣ Easy Maintenance

3️⃣ Easy Testing

4️⃣ Easy Extension

5️⃣ Better Architecture

----------------------------------------------------------
🧩 Relationship Used Here
----------------------------------------------------------

📌 Notification ---> MessageService

Relationship:
✅ ASSOCIATION

Reason:
Notification receives MessageService from outside.

----------------------------------------------------------

📌 EmailService ---> MessageService

Relationship:
✅ INHERITANCE

Reason:
EmailService inherits MessageService interface.

----------------------------------------------------------

📌 SMSService ---> MessageService

Relationship:
✅ INHERITANCE

----------------------------------------------------------

📌 WhatsAppService ---> MessageService

Relationship:
✅ INHERITANCE

----------------------------------------------------------

📌 Notification HAS-A MessageService

Relationship:
✅ ASSOCIATION
(Dependency Injection)

Reason:
Service is injected through constructor.

==========================================================
💻 CODE STARTS HERE
==========================================================
"""

from abc import ABC, abstractmethod


# ==========================================================
# 🎯 ABSTRACTION
# ==========================================================
# All messaging services must follow this contract.
#
# This is the most important part of DIP.
#
# High-level modules will depend on this abstraction,
# not on concrete implementations.
# ==========================================================

class MessageService(ABC):

    @abstractmethod
    def send(self, message):
        pass


# ==========================================================
# 📧 EMAIL SERVICE
# ==========================================================
#
# Relationship:
# EmailService IS-A MessageService
#
# Type:
# ✅ Inheritance
#
# Responsibility:
# Send messages using Email
# ==========================================================

class EmailService(MessageService):

    def send(self, message):
        print(f"📧 Email Sent: {message}")


# ==========================================================
# 📱 SMS SERVICE
# ==========================================================
#
# Relationship:
# SMSService IS-A MessageService
#
# Type:
# ✅ Inheritance
#
# Responsibility:
# Send messages using SMS
# ==========================================================

class SMSService(MessageService):

    def send(self, message):
        print(f"📱 SMS Sent: {message}")


# ==========================================================
# 💬 WHATSAPP SERVICE
# ==========================================================
#
# Relationship:
# WhatsAppService IS-A MessageService
#
# Type:
# ✅ Inheritance
#
# Responsibility:
# Send messages using WhatsApp
# ==========================================================

class WhatsAppService(MessageService):

    def send(self, message):
        print(f"💬 WhatsApp Message Sent: {message}")


# ==========================================================
# 🔔 HIGH LEVEL MODULE
# ==========================================================
#
# Notification should NOT know whether
# messages are sent by:
#
# - Email
# - SMS
# - WhatsApp
#
# It only knows:
#
# "I need something that follows
# MessageService interface."
#
# Relationship:
# Notification HAS-A MessageService
#
# Type:
# ✅ Association
#
# Why Association?
#
# Because service comes from outside
# and is passed into constructor.
#
# This is Constructor Dependency Injection.
# ==========================================================

class Notification:

    def __init__(self, service: MessageService):

        # Dependency Injection happens here
        self.service = service

    def send(self, message):

        # Delegation
        self.service.send(message)


# ==========================================================
# 🚀 EXAMPLE 1
# EMAIL
# ==========================================================

print("\n========== EMAIL EXAMPLE ==========\n")

email_service = EmailService()

notification = Notification(email_service)

notification.send("Welcome User")


# ==========================================================
# 🚀 EXAMPLE 2
# SMS
# ==========================================================

print("\n========== SMS EXAMPLE ==========\n")

sms_service = SMSService()

notification = Notification(sms_service)

notification.send("OTP: 123456")


# ==========================================================
# 🚀 EXAMPLE 3
# WHATSAPP
# ==========================================================

print("\n========== WHATSAPP EXAMPLE ==========\n")

whatsapp_service = WhatsAppService()

notification = Notification(whatsapp_service)

notification.send("Your order has been delivered.")


# ==========================================================
# 🚀 EXAMPLE 4
# ADDING NEW SERVICE
# ==========================================================
#
# Notice:
# Notification class does NOT change.
#
# We simply create a new service.
#
# This proves:
# ✅ Open for Extension
# ✅ Closed for Modification
#
# DIP + OCP work together.
# ==========================================================

class TelegramService(MessageService):

    def send(self, message):
        print(f"🚀 Telegram Message Sent: {message}")


print("\n========== TELEGRAM EXAMPLE ==========\n")

telegram_service = TelegramService()

notification = Notification(telegram_service)

notification.send("Hello from Telegram")


# ==========================================================
# 🎯 FINAL SUMMARY
# ==========================================================
#
# BAD DESIGN
#
# Notification ---> EmailService
#
# Tight Coupling
#
# ----------------------------------------------------------
#
# GOOD DESIGN
#
# Notification ---> MessageService
#
#                     ▲
#                     │
#     ┌───────────────┼───────────────┐
#     │               │               │
#     ▼               ▼               ▼
# EmailService   SMSService   WhatsAppService
#
# ----------------------------------------------------------
#
# Benefits:
#
# ✅ Loose Coupling
# ✅ Easy Testing
# ✅ Easy Maintenance
# ✅ Easy Extension
# ✅ Better Architecture
# ✅ Scalable Design
#
# This is Dependency Inversion Principle (DIP).
#
# Remember:
#
# "Depend on Abstractions,
#  Not on Concrete Implementations."
#
# ==========================================================
