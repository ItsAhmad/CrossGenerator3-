document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('partNumberForm');
    const resultsContainer = document.getElementById('results');

    form.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Collect input data
        const model = document.getElementById('model').value;
        const mounting = document.getElementById('mounting').value;
        const diffuser = document.getElementById('diffuser').value;
        const lamp = document.getElementById('lamp').value;
        const driver = document.getElementById('driver').value; 
        const voltage = document.getElementById('voltage').value;
        const doorframe = document.getElementById('doorframe').value;
        const options = document.getElementById('options').value;
        const accessories = document.getElementById('accessories').value;


        if (!model) {
            alert('Please provide the model part number.');
            return;
        }
        
        if (!mounting) {
            alert('Please provide the mounting part number.');
            return;
        }
        
        if (!diffuser) {
            alert('Please provide the diffuser part number.');
            return;
        }
        
        if (!lamp) {
            alert('Please provide the lamp part number.');
            return;
        }
        
        if (!driver) {
            alert('Please provide the driver part number.');
            return;
        }
        
        if (!voltage) {
            alert('Please provide the voltage part number.');
            return;
        }
        
        if (!doorframe) {
            alert('Please provide the doorframe part number.');
            return;
        }
        
        if (!options) {
            alert('Please provide the options part number.');
            return;
        }

        if (!accessories) {
            alert('Please provide the accessories part number.');
            return;
        }
        

        try {
            // Send data to the server
            const response = await fetch('/api/search-part', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ model }),
            });

            if (response.ok) {
                const data = await response.json();
                resultsContainer.innerHTML = ''; // Clear previous results

                // Display the equivalent part number
                if (data.amicoPartNumber) {
                    const resultItem = document.createElement('li');
                    resultItem.textContent = `Equivalent Amico Part Number: ${data.amicoPartNumber}`;
                    resultsContainer.appendChild(resultItem);
                } else {
                    resultsContainer.textContent = 'No equivalent part found.';
                }
            } else {
                alert('Error: Could not retrieve part information.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while searching for the part.');
        }
    });
});

  
