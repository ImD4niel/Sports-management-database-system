#!/usr/bin/env python
"""
Setup script for SportsHub - Sports Management System
Run this script to set up the project for development or production.
"""

import os
import sys
import subprocess
import secrets
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def create_env_file():
    """Create a .env file with default values."""
    env_file = Path(".env")
    if not env_file.exists():
        print("🔄 Creating .env file...")
        secret_key = secrets.token_urlsafe(50)
        env_content = f"""# Django Settings
SECRET_KEY={secret_key}
DEBUG=True

# Email Configuration (optional)
SENDGRID_API_KEY=your-sendgrid-api-key-here

# Contact Information
CONTACT_EMAIL=admin@sportsmanagement.com
ADMIN_EMAIL=admin@sportsmanagement.com
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created with default values")
    else:
        print("ℹ️  .env file already exists")

def main():
    """Main setup function."""
    print("🚀 Setting up SportsHub - Sports Management System")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    
    # Create virtual environment if it doesn't exist
    venv_path = Path("venv")
    if not venv_path.exists():
        if not run_command("python -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("ℹ️  Virtual environment already exists")
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("⚠️  Failed to install dependencies. Please check requirements.txt")
    
    # Create .env file
    create_env_file()
    
    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        print("⚠️  Failed to run migrations. Please check your database configuration")
    
    print("\n🎉 Setup completed!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    print("   - Windows: venv\\Scripts\\activate")
    print("   - Unix/Mac: source venv/bin/activate")
    print("2. Create a superuser: python manage.py createsuperuser")
    print("3. Start development server: python manage.py runserver")
    print("4. Open http://localhost:8000 in your browser")
    print("\nFor production deployment, see the README.md file.")

if __name__ == "__main__":
    main()
