from app import app

# For Vercel WSGI compatibility
app = app.wsgi_app
