# Student Incentive System

A Flask-based CLI application to manage student volunteer hours. The system allows students to request volunteer hours and track progress, while staff can review, approve, or deny requests. A leaderboard ranks students based on confirmed hours, with accolades awarded for milestones.

---

## 📌 Features

### Student Management

* 👩‍🎓 Create student accounts
* 📝 Request volunteer hours
* 📊 View personal profile (pending/confirmed hours, accolades, leaderboard rank)

### Staff Management

* 👨‍💼 Create staff accounts
* ✅ Review student hours (approve/deny with password authentication)
* 🗑️ Delete student accounts

### Leaderboard & Accolades

* 🏆 Students ranked by confirmed hours
* 🥉 Bronze (10+), 🥈 Silver (25+), 🥇 Gold (50+) accolades automatically awarded

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment

**On Linux/Mac:**

```bash
export FLASK_APP=wsgi.py
```

**On Windows (PowerShell):**

```powershell
$env:FLASK_APP="wsgi.py"
```

### 4. Initialize database with sample data

```bash
flask init
```

This will drop all tables, recreate them, and seed sample staff, students, and confirmed hours.

---

## 🖥️ CLI Commands

All commands are run using:

```bash
flask <command>
```

### 🔹 Initialization

| Command      | Description                                  |
| ------------ | -------------------------------------------- |
| `flask init` | Reset and seed the database with sample data |

### 🔹 Student Commands

| Command                       | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| `flask student create`        |  Create a new student account (prompts for name + password)        |
| `flask student profile`       |  Display Student profile including accolades, rank, total hours, etc|   |
| `flask student request_hours` |  Request volunteer hours (student ID, hours, activity)             |

**Sample student profile output:**

```text
_____Alice Brown's Profile_____

Pending Hours:
- Beach Cleanup: 5 hours

Confirmed Hours:
- Tree Planting: 12 hours
- Food Drive: 7 hours

Total Confirmed Hours: 19
Accolade: Bronze (Awarded on: 2025-09-29)
Leaderboard Rank: #2
```

### 🔹 Staff Commands

| Command                      | Description                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `flask staff create`         | Create a new staff account (prompts for name + password)                       |
| `flask staff review_hours`   | Review pending student hours (approve/deny by request ID, password required)   |
| `flask staff delete_student` | Delete a student account (requires staff ID + student ID)                      |

**Sample review_hours output:**

```text
Pending requests for Alice Brown:
[Request ID: 3] 5h - Beach Cleanup

Do you want to confirm or deny? (c/d): c
Confirmed 5h - Beach Cleanup for Alice Brown.
```

### 🔹 Utility Commands

| Command               | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `flask list_students` |    List all students                                         |
| `flask list_staff`    |       List all staff                                         |
| `flask leaderboard`   |    Show ranked leaderboard (name, accolade, confirmed hours) |

**Sample leaderboard output:**

```text
_____ Leaderboard _____
1. Alice Brown [Bronze] - 19 hours
2. Bob Green [Bronze] - 18 hours
3. Jane Doe [None] - 11 hours
4. Joe Mama [None] - 2 hours
```

---

## 🏅 Accolade Levels

* 🥉 Bronze → 10+ confirmed hours
* 🥈 Silver → 25+ confirmed hours
* 🥇 Gold → 50+ confirmed hours

Accolades are automatically awarded when students reach milestones.

---

## 🔧 Example Workflow

1. **Create staff**

```bash
flask staff create
```

2. **Create student**

```bash
flask student create
```

3. **Student requests hours**

```bash
flask student request_hours
```

4. **Staff reviews request**

```bash
flask staff review_hours
```

5. **Student views profile & leaderboard**

```bash
flask student profile
flask leaderboard
```

---

## 🛠️ Tech Stack

* Flask (Web Framework & CLI)
* Flask-SQLAlchemy (ORM for database)
* Flask-Migrate (Database migrations)
* Click (CLI command handling)
* Werkzeug Security (Password hashing)
