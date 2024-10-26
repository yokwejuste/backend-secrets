[Back to Main README](../README.md)

# SMS

This folder contains Python scripts for integrating various SMS service providers to send text messages. Each script provides functions for sending SMS using different API clients.

## Contents

- [Africa's Talking](#africas-talking)
- [AWS SNS](#aws-sns)
- [Azure SMS](#azure-sms)
- [Nexmo (Vonage)](#nexmo-vonage)
- [Twilio](#twilio)

---

### Africa's Talking

**Africa's Talking** is a communication API platform providing SMS, voice, and USSD services primarily across Africa.

- **File**: `africastalking_sms.py`
- **Setup**:
  1. Install `africastalking` library: `pip install africastalking`.
  2. Configure API key and username.

- **Example Usage**:
  ```python
  from africastalking_sms import send_sms
  send_sms("recipient_number", "Your message here")
  ```

---

### AWS SNS

**AWS SNS (Simple Notification Service)** allows for sending SMS messages to users worldwide.

- **File**: `aws_sms.py`
- **Setup**:
  1. Install AWS SDK: `pip install boto3`.
  2. Configure AWS credentials with access to SNS.

- **Example Usage**:
  ```python
  from aws_sms import send_sms
  send_sms("recipient_number", "Your message here")
  ```

---

### Azure SMS

**Azure Communication Services** enables SMS messaging through the Azure cloud infrastructure.

- **File**: `azure_sms.py`
- **Setup**:
  1. Install Azure SDK: `pip install azure-communication-sms`.
  2. Configure Azure Communication Services connection string.

- **Example Usage**:
  ```python
  from azure_sms import send_sms
  send_sms("recipient_number", "Your message here")
  ```

---

### Nexmo (Vonage)

**Nexmo** (now Vonage) provides APIs for SMS, voice, and messaging services.

- **File**: `nexmo_sms.py`
- **Setup**:
  1. Install `vonage` library: `pip install vonage`.
  2. Configure API key and secret.

- **Example Usage**:
  ```python
  from nexmo_sms import send_sms
  send_sms("recipient_number", "Your message here")
  ```

---

### Twilio

**Twilio** is a popular cloud communications platform, allowing you to send SMS, voice, and other messaging services.

- **File**: `twilio_sms.py`
- **Setup**:
  1. Install Twilio SDK: `pip install twilio`.
  2. Configure Twilio account SID, auth token, and messaging service SID or sender number.

- **Example Usage**:
  ```python
  from twilio_sms import send_sms
  send_sms("recipient_number", "Your message here")
  ```

---

## How to Use

1. Clone the repository and navigate to the `sms` folder.
2. Install any required dependencies as mentioned in each section.
3. Configure your credentials for each SMS provider.
4. Run the scripts to send SMS messages using the specified provider.

## Contributing

Contributions are welcome! If you’d like to add more SMS providers or enhance existing implementations, please submit a pull request with a detailed description of your changes.
