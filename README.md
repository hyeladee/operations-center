# Operations Center

**A lightweight, modular Django suite** for tracking car hires, hotel bookings, office expenses, and overall operations, protected with a strong authentication system.

---

## ✨ Live Demo

Checkout live project here: [Operations Center](https://ops-tracker-p017.onrender.com)

---

## 🚀 Quickstart

### 1. Clone the Repo

```bash
git clone https://github.com/hyeladee/operations-center.git
cd operations-center
```

### 2. Install Dependencies

Using Pipenv:

```bash
pipenv install
```

Install Node modules (for Tailwind CSS):

```bash
dev-mode:
npx @tailwindcss/cli -i ./static/css/tailwind-input.css -o ././static/css/tailwind-output.css --watch

production:
npx @tailwindcss/cli -i ./static/css/tailwind-input.css -o ././static/css/tailwind-output.css --minify
```

### 3. Configure Environment

Copy the env template and fill in your secrets:

```bash
cp .env.example .env
```

### 4. Migrate & Run

```bash
python manage.py migrate
python manage.py runserver

# if you prefer a production ready server
uvicorn operationsTracker.asgi:application --host 0.0.0.0 --port 8000
```

---

## 📁 Project Structure

* **trackerApp/**: Main Django project (settings, URLs)
* **carHires/**: Manage car hire requests
* **hotelBookings/**: Hotel booking logs
* **officeExpenses/**: Office expense reports
* **operationsTracker/**: Dashboard and analytics
* **templates/**: Shared + app-specific HTML templates
* **static/**: Tailwind CSS & other assets

---

## 🔧 Key Configs

* **Tailwind CSS** integrated via `npm`
* Environment variables loaded via `.env`
* App routes registered in `trackerApp/urls.py`
* Static files served at `/static/`

---

## 📊 Usage

* Admin panel: `/admin/`
* App endpoints:

  * `/car-hire/`
  * `/hotel-booking/`
  * `/office-expense/`
  * `/ops-tracker/`
* Templates extend `base.html` with Tailwind styling blocks

---

## 🚀 Tech Stack

* **Python 3**, **Django**
* **Tailwind CSS**, **npx**
* **Pipenv** for dependency management
* **Render** for live hosting

---

## 🙌 Features

* CRUD for car, hotel, and expense tracking
* Central dashboard for operations
* Tailwind-powered responsive design
* Modular architecture for easy extension

---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch
3. Push your changes
4. Submit a pull request

---

## 📄 License

MIT License © 2025 [hyeladee](https://github.com/hyeladee)
