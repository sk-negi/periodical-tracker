# Periodical Tracker

A web-based application for tracking newspapers and periodicals received by libraries.

## Problem Statement

Many libraries still rely on Excel spreadsheets to track incoming newspapers and periodicals, leading to cluttered sheets where data entry is error-prone and accidental changes are common. A simple web-based application with a SQL database offers a more elegant solution—providing clean data entry forms, preventing accidental edits to existing records, and enabling easy access from mobile devices or tablets for staff working at receiving desks. This proof-of-concept demonstrates how basic web technologies can modernize routine library workflows while maintaining simplicity.

## Features

- Add new periodical/newspaper records
- View all records in a sortable table
- Edit existing records
- Export data to CSV
- Mobile-friendly interface

## Tech Stack

- **Backend:** Python + Flask
- **Database:** SQLite
- **Frontend:** HTML templates (Jinja2) + CSS
- **Export:** CSV

## Status

🚧 **In Development** - This is a proof-of-concept project.

## Data Fields

- Type (Newspaper/Periodical)
- Title
- Vendor
- Issue/Volume (optional)
- Date Received
- Status (Received/Not Received)
- Entered By
- Notes (optional)

## Author

Built as a portfolio project to demonstrate library technology solutions.
