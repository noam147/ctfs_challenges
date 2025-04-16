const optionRadios = document.getElementsByName('option');
const usernameInput = document.getElementById('usernameInput');

optionRadios.forEach(radio => {
  radio.addEventListener('change', () => {
    usernameInput.style.display = radio.value === '2' ? 'block' : 'none';
  });
});

const dateToggle = document.getElementById('dateRangeToggle');
const dateInputs = document.getElementById('dateInputs');
const startDateInput = document.getElementById('startDate');
const endDateInput = document.getElementById('endDate');

function getTodayDate() {
  const today = new Date();
  return `${String(today.getDate()).padStart(2, '0')}/${String(today.getMonth() + 1).padStart(2, '0')}/${today.getFullYear()}`;
}

dateToggle.addEventListener('change', () => {
  if (dateToggle.checked) {
    dateInputs.style.display = 'block';
    startDateInput.value = getTodayDate();
    endDateInput.value = getTodayDate();
  } else {
    dateInputs.style.display = 'none';
    startDateInput.value = '';
    endDateInput.value = '';
  }
});

document.getElementById('uploadForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const file = document.getElementById('chatfile').files[0];
    if (!file) return;

    const selectedOption = document.querySelector('input[name="option"]:checked').value;
    const username = document.getElementById('username').value;

    const formData = new FormData();
    formData.append('chatfile', file);
    formData.append('option', selectedOption);
    if (selectedOption === '2') formData.append('username', username);
    if (dateToggle.checked) {
      formData.append('startDate', startDateInput.value);
      formData.append('endDate', endDateInput.value);
    }

    document.getElementById('uploadForm').style.display = 'none';
    document.getElementById('loading').style.display = 'block';

    fetch('/upload', {
      method: 'POST',
      body: formData
    })
    .then(response => response.json())
    .then(data => {

      document.getElementById('loading').style.display = 'none';
      document.getElementById('result').style.display = 'block';
        if (data.success) {
            // Redirect if successful
            window.location.href = data.link; // e.g., "/link"
        } else {
            // Show error message
            document.getElementById('result').innerHTML = `<strong>Error:</strong> ${data.message || 'Try again.'}`;
        }
    })
    .catch(err => {
      document.getElementById('loading').style.display = 'none';
      document.getElementById('result').style.display = 'block';
      document.getElementById('result').innerHTML = `Something went wrong: ${err}`;
    });
});