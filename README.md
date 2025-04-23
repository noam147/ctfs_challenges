# CTF Web & Forensics Challenges Platform

This project is a Capture the Flag (CTF) challenge platform focused on web security and digital forensics. It is designed to provide hands-on experience through realistic, scenario-based tasks.

## Technologies Used

- **Frontend:** HTML, JavaScript  
- **Backend:** Python (Flask, FastAPI, or similar)  
- **Hosting:** AWS Virtual Machine with a public IP address

## Live Deployment

The project is hosted on an AWS VM and is accessible via the following URL:
http://13.51.79.222:5000/

.
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── my_ctfs/                  # Main directory containing all CTF content
│   ├── menu/                 # Menu and navigation logic for available challenges
│   └── <challenge_name>/     # Each folder represents an individual CTF challenge
│       ├── app.py            # Backend application file for the challenge
│       ├── solution.txt      # Brief explanation of the challenge solution
│       ├── images/           # Optional folder for challenge-specific images
│       └── templates/        # HTML files used in the challenge
│           ├── index.html
│           └── ...

