import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

from src.service.services_constants import services_constants

load_dotenv()

# def send_email_booking(booking_data, car_data):
#     subject = "Новая заявка на бронирование автомобиля"

#     from_reserve_formatted = booking_data.from_reserve.strftime("%d.%m.%Y %H:%M")
#     to_reserve_formatted = booking_data.to_reserve.strftime("%d.%m.%Y %H:%M")
    
#     message = f"Заявка на бронирование автомобиля:\n\n"
#     message += f"Клиент: {booking_data.first_name} {booking_data.last_name}\n"
#     message += f"Телефон: {booking_data.phone}\n"
#     message += f"Email: {booking_data.email}\n"
#     message += f"Дата приема автомобиля: {from_reserve_formatted}\n"
#     message += f"Дата сдачи автомобиля: {to_reserve_formatted}\n"
#     message += f"Сумма: {int(booking_data.total_amount)} р.\n"
    
#     message += f"Марка автомобиля: {car_data.brand}\n"
#     message += f"Модель автомобиля: {car_data.model}\n"

#     msg = MIMEMultipart()
#     msg['From'] = os.getenv('EMAIL_FROM')
#     msg['To'] = os.getenv('EMAIL_TO')
#     msg['Subject'] = subject

#     msg.attach(MIMEText(message, 'plain'))

#     try:
#         server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
#         server.starttls()
#         server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
#         server.sendmail(os.getenv('EMAIL_FROM'), [os.getenv('EMAIL_TO')], msg.as_string())
#         server.quit()
#         print("Письмо успешно отправлено")
#     except Exception as e:
#         print(f"Ошибка при отправке письма: {str(e)}")

def send_email_booking(booking_data, car_data, services_constants):
    subject = "Новая заявка на бронирование автомобиля"

    from_reserve_formatted = booking_data.from_reserve.strftime("%d.%m.%Y %H:%M")
    to_reserve_formatted = booking_data.to_reserve.strftime("%d.%m.%Y %H:%M")
    
    message = f"Заявка на бронирование автомобиля:\n\n"
    message += f"Клиент: {booking_data.first_name} {booking_data.last_name}\n"
    message += f"Телефон: {booking_data.phone}\n"
    message += f"Email: {booking_data.email}\n"
    message += f"Дата приема автомобиля: {from_reserve_formatted}\n"
    message += f"Дата сдачи автомобиля: {to_reserve_formatted}\n"
    message += f"Сумма: {int(booking_data.total_amount)} р.\n"
    
    message += f"Марка автомобиля: {car_data.brand}\n"
    message += f"Модель автомобиля: {car_data.model}\n"

    # Добавляем информацию о выбранных дополнительных услугах и их стоимости
    message += "\nВыбранные дополнительные услуги:\n"
    for service, count in booking_data.additional_services.items():
        if count > 0:
            cost = services_constants.get(service, 0) * count
            message += f"- {service}: {count} раз, на сумму {cost} руб.\n"

    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_FROM')
    msg['To'] = os.getenv('EMAIL_TO')
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT')))
        server.starttls()
        server.login(os.getenv('SMTP_USERNAME'), os.getenv('SMTP_PASSWORD'))
        server.sendmail(os.getenv('EMAIL_FROM'), [os.getenv('EMAIL_TO')], msg.as_string())
        server.quit()
        print("Письмо успешно отправлено")
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")