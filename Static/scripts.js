// scripts.js

function fetchCustomers() {
    fetch('/fetch_customers')
        .then(response => response.json())
        .then(data => {
            const customersList = document.getElementById('customersList');
            customersList.innerHTML = '';
            data.forEach(customer => {
                customersList.innerHTML += `<p>${customer.Cname} - Phone: ${customer.Phone}, Mobile: ${customer.Mobile}, Address: ${customer.Address}</p>`;
            });
        })
        .catch(error => console.error('Error fetching customers:', error));
}

function fetchCars() {
    fetch('/fetch_cars')
        .then(response => response.json())
        .then(data => {
            const carsList = document.getElementById('carsList');
            carsList.innerHTML = '';
            data.forEach(car => {
                carsList.innerHTML += `<p>VIN: ${car.VIN}, Model: ${car.Model}, Type: ${car.Car_type}, Colour: ${car.Colour}, Owner: ${car.OwnerName}</p>`;
            });
        })
        .catch(error => console.error('Error fetching cars:', error));
}
