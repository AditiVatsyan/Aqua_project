import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test if home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200

def test_booking_page(client):
    """Test if booking page loads correctly"""
    response = client.get('/booking')
    assert response.status_code == 200
    assert b"Book Your Ride" in response.data  # Checking page content

def test_booking_submission(client):
    """Test booking form submission"""
    response = client.post('/booking', data={
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'phone': '1234567890',
        'ride': 'Ferris Wheel',
        'date': '2025-04-15'
    })
    assert response.status_code == 200
    assert b"confirmation" in response.data  # Checking if confirmation page loads

def test_email_function():
    """Test email sending function"""
    from app import send_confirmation_email
    result = send_confirmation_email("John Doe", "test@example.com", "Ferris Wheel", "2025-04-15")
    assert result is True  # Email should send successfully
