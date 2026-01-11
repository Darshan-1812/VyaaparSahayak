"""
VyaaparSahayak Backend Server
Starts the FastAPI application with Uvicorn
"""

import uvicorn
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """Start the FastAPI server"""
    print("=" * 60)
    print("🚀 Starting VyaaparSahayak Backend Server")
    print("=" * 60)
    print("📍 Server URL: http://127.0.0.1:8000")
    print("📚 API Docs: http://127.0.0.1:8000/docs")
    print("=" * 60)
    print()
    
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )

if __name__ == "__main__":
    main()
