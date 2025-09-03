# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django/Wagtail CMS project for a hotel resort website. It uses:
- **Django 5.2.4** as the web framework
- **Wagtail 7.1+** as the content management system
- **TailwindCSS 4.1** for styling
- **SQLite** for development database
- **WhiteNoise** for static file serving

## Development Commands

### Python/Django Commands
```bash
# Activate virtual environment first
source venv/bin/activate

# Run development server (uses dev settings by default)
python manage.py runserver

# Create/apply database migrations  
python manage.py makemigrations
python manage.py migrate

# Create superuser (custom command available)
python manage.py makesuperuser

# Collect static files
python manage.py collectstatic
```

### Frontend/CSS Commands
```bash
# Watch and compile Tailwind CSS during development
npm run dev

# Build production-ready CSS
npm run build
```

## Project Structure

The project follows Django/Wagtail conventions:

- **`resort/`** - Main Django project directory containing settings and configuration
  - **`settings/`** - Split settings: `base.py`, `dev.py`, `production.py`
  - **`static/`** - Project-level static files including Tailwind CSS
- **`home/`** - Wagtail app containing the HomePage model and homepage functionality
- **`search/`** - Search functionality with Wagtail's built-in search backend
- **`templates/`** - Project-level templates including `base.html` and error pages

## Settings Configuration

The project uses Django's split settings pattern:
- Development uses `resort.settings.dev` (set as default in `manage.py`)
- Base configuration is in `resort.settings.base`
- Production settings are in `resort.settings.production`

## Styling System

TailwindCSS is configured to scan:
- `resort/templates/**/*.html`
- `home/templates/**/*.html`

Custom theme variables are defined in `resort/static/css/input.css`:
- `--color-brand: #e9ce7e` (gold color for branding)

The CSS build process outputs to `resort/static/css/output.css`.

## Database & Migrations

Currently uses SQLite for development. The project has custom migrations in the `home` app for initial setup.

## Key Wagtail Configuration

- Site name: "resort"
- Search backend: Database backend (not Elasticsearch)
- Admin base URL configured for production deployment
- Standard Wagtail apps enabled: forms, redirects, embeds, etc.