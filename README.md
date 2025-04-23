# CTF Web & Forensics Challenges Platform

This project is a Capture the Flag (CTF) challenge platform focused on web security and digital forensics. It is designed to provide hands-on experience through realistic, scenario-based tasks.

## Technologies Used

- **Frontend:** HTML, JavaScript  
- **Backend:** Python (Flask, FastAPI, or similar)  
- **Hosting:** AWS Virtual Machine with a public IP address

## Live Deployment

The project is hosted on an AWS VM and is accessible via the following URL:
http://13.51.79.222:5000/

## Skills for Solving

The following skills will help you successfully solve the challenges in this project:

- **Digital Forensics**: Analyzing digital evidence, such as images, files, and hashes, to uncover hidden information.
- **Python Programming**: Writing scripts to automate analysis and solve complex problems. Familiarity with libraries such as **Flask**, **Pillow**, and **requests** is beneficial.
- **Basic Web Security**: Understanding common vulnerabilities like **SQL injection**, **XSS**, and **CSRF**, and how to exploit them to retrieve flags.

---

## Tools Recommended for Solvers

To tackle the challenges efficiently, the following tools are highly recommended:

- **Burp Suite**: A powerful tool for web security testing, especially for tasks like vulnerability scanning, proxying, and exploitation of web application flaws.
- **PyCharm**: A Python IDE that simplifies development, debugging, and testing of Python scripts and web applications.
- **Hex-Dump**: A tool for examining binary data and analyzing file content, especially useful for understanding file structures and performing low-level forensics analysis.

---

```
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
├── requirements.txt          # Python dependencies
```
