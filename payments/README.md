[Back to Main README](../README.md)

# Payments

This folder contains Python scripts for integrating various payment providers, including traditional gateways, local payment methods, and cryptocurrency payments. Each script provides functions for initiating and managing transactions with different payment providers.

## Contents

- [Braintree](#braintree)
- [BTCPay](#btcpay)
- [Chargebee](#chargebee)
- [GetLago](#getlago)
- [M-Pesa](#m-pesa)
- [MTN MoMo](#mtn-momo)
- [Orange Money](#orange-money)
- [PayPal](#paypal)
- [Paystack](#paystack)
- [Razorpay](#razorpay)
- [Square](#square)
- [Stripe](#stripe)

---

### Braintree

**Braintree** is a full-stack payment platform that makes it easy to accept payments online.

- **File**: `braintree_payment.py`
- **Setup**:
  1. Install the Braintree SDK: `pip install braintree`.
  2. Configure Braintree credentials (merchant ID, public key, private key).

- **Example Usage**:
  ```python
  from braintree_payment import create_transaction
  create_transaction(100, "USD", "payment_method_nonce")
  ```

---

### BTCPay

**BTCPay** is a cryptocurrency payment processor that allows businesses to accept Bitcoin and other cryptocurrencies.

- **File**: `btcpay_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Set up BTCPay server and API keys.

- **Example Usage**:
  ```python
  from btcpay_payment import create_invoice
  create_invoice(0.01, "BTC")
  ```

---

### Chargebee

**Chargebee** is a subscription management and recurring billing software for SaaS businesses.

- **File**: `chargebee_payment.py`
- **Setup**:
  1. Install Chargebee Python library: `pip install chargebee`.
  2. Configure API key and site name.

- **Example Usage**:
  ```python
  from chargebee_payment import create_subscription
  create_subscription("plan_id", "customer_id")
  ```

---

### GetLago

**GetLago** is an open-source billing API for managing subscription billing and usage-based billing.

- **File**: `getlago_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Configure API key.

- **Example Usage**:
  ```python
  from getlago_payment import create_invoice
  create_invoice("customer_id", 2000, "USD")
  ```

---

### M-Pesa

**M-Pesa** is a mobile money service that allows users to transfer money and make payments.

- **File**: `mpesa_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Configure M-Pesa API credentials.

- **Example Usage**:
  ```python
  from mpesa_payment import initiate_payment
  initiate_payment("254700000000", 1000)
  ```

---

### MTN MoMo

**MTN MoMo** provides mobile money services that allow users to make payments and transfers using mobile devices.

- **File**: `mtn_momo_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Configure MTN MoMo API credentials.

- **Example Usage**:
  ```python
  from mtn_momo_payment import request_payment
  request_payment("256700000000", 500)
  ```

---

### Orange Money

**Orange Money** is a mobile money service that allows users to send and receive money, pay bills, and more.

- **File**: `orange_money_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Configure Orange Money API credentials.

- **Example Usage**:
  ```python
  from orange_money_payment import initiate_transaction
  initiate_transaction("237600000000", 1500)
  ```

---

### PayPal

**PayPal** is a widely used online payment platform for individuals and businesses.

- **File**: `paypal_payment.py`
- **Setup**:
  1. Install PayPal SDK: `pip install paypalrestsdk`.
  2. Configure PayPal client ID and secret.

- **Example Usage**:
  ```python
  from paypal_payment import create_payment
  create_payment(50, "USD")
  ```

---

### Paystack

**Paystack** is a Nigerian payment gateway that makes it easy for businesses in Africa to accept payments.

- **File**: `paystack_payment.py`
- **Setup**:
  1. Install requests: `pip install requests`.
  2. Configure Paystack API key.

- **Example Usage**:
  ```python
  from paystack_payment import initialize_transaction
  initialize_transaction(10000, "NGN", "user@example.com")
  ```

---

### Razorpay

**Razorpay** provides payment solutions for businesses to accept, process, and disburse payments.

- **File**: `razorpay_payment.py`
- **Setup**:
  1. Install Razorpay SDK: `pip install razorpay`.
  2. Configure Razorpay key ID and secret.

- **Example Usage**:
  ```python
  from razorpay_payment import create_order
  create_order(50000, "INR")
  ```

---

### Square

**Square** is a popular payment platform for accepting payments, managing invoices, and processing transactions.

- **File**: `squareup_payment.py`
- **Setup**:
  1. Install Square SDK: `pip install squareup`.
  2. Configure Square access token.

- **Example Usage**:
  ```python
  from squareup_payment import create_payment
  create_payment(100, "USD", "nonce_from_card")
  ```

---

### Stripe

**Stripe** is a payment processor for online and in-person payments, supporting various currencies and payment methods.

- **File**: `stripe_payment.py`
- **Setup**:
  1. Install Stripe SDK: `pip install stripe`.
  2. Configure Stripe API key.

- **Example Usage**:
  ```python
  from stripe_payment import charge_card
  charge_card(2000, "usd", "card_token")
  ```

---

## How to Use

1. Clone the repository and navigate to the `payments` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure your credentials for each payment provider.
4. Run the scripts to initiate transactions with the specified payment provider.

## Contributing

Contributions are welcome! If you’d like to add more payment providers or enhance existing implementations, please submit a pull request with a detailed description of your changes.
