from flask import Flask, request, render_template, redirect, url_for
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
app = Flask(__name__)

# Configure your email settings
EMAIL_ADDRESS = 'aditisharma@gmail.com'  # Replace with your email
EMAIL_PASSWORD = 'gezl itfq mmms cftt'  # Replace with your email password

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ride1')  
def ride1():
    return render_template('ride1.html')

@app.route('/ride2')  
def ride2():
    return render_template('ride2.html')

@app.route('/ride3')
def ride3():
    return render_template('ride3.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        ride = request.form['ride']
        date = request.form['date']
        
        # Store data in CSV
        with open('bookings.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, phone, ride, date])
        
        # Send confirmation email
        send_confirmation_email(name, email, ride, date)
        
        return render_template('confirmation.html', name=name)
    
    return render_template('booking.html')

# Function to send confirmation email
def send_confirmation_email(name, email, ride, date):
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Ride Booking Confirmation"
        
        body = f"Dear {name},\n\nYour booking for the '{ride}' ride on {date} has been confirmed. Thank you for booking with FunCity!\n\nBest regards,\nFunCity Team"
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"Confirmation email sent to {email}")
        return True
    except Exception as e:
        print(f"Email sending error: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True)
  


