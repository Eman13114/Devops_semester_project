from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Sample data - in a real app, this would typically come from a database
items = [
    {
        'id': 1,
        'title': 'Project Alpha',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 2,
        'title': 'Project Beta',
        'description': 'Innovation at its finest',
        'date': '2025-03-13'
    },
    {
        'id': 3,
        'title': 'Project Gamma',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 4,
        'title': 'Project Delta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 5,
        'title': 'Project Epsilon',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 6,
        'title': 'Project Zeta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 7,
        'title': 'Project Eta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 8,
        'title': 'Project Theta',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 9,
        'title': 'Project Iota',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
    {
        'id': 10,
        'title': 'Project Kappa',
        'description': 'A groundbreaking initiative',
        'date': '2025-03-13'
    },
