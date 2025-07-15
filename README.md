# Trade Opportunities API - Final README

This project is a FastAPI-based service that provides market trade opportunity reports for various sectors in India. It is built to demonstrate clean API design, AI analysis integration, security implementation, and rate-limited access.

## Project Purpose

The purpose of this project is to create a RESTful API that:
- Accepts a sector name like "pharmaceuticals" or "technology"
- Searches for current market news or data related to that sector
- Uses AI (mocked in this version) to generate insights
- Returns a structured market analysis in markdown format

## Features Implemented

1. **FastAPI Web Application**  
   A FastAPI server with asynchronous route handling and Swagger UI auto-generated at `/docs`.

2. **Single Endpoint**  
   The API provides one endpoint `/analyze/{sector}` which takes a sector name as input and returns a structured analysis.

3. **Security**  
   The endpoint is protected with Bearer Token authentication. The token value is stored securely in a `.env` file. Only requests with a valid token can access the analysis.

4. **Rate Limiting**  
   Each client is limited to a defined number of requests per minute using the `slowapi` library. This prevents abuse and spam access.

5. **Input Validation**  
   The `sector` input is validated to ensure only alphabetical strings are allowed.

6. **AI Analysis Integration (Mocked)**  
   The application simulates analysis using a placeholder AI function. It can later be connected to real APIs like Google Gemini or OpenAI for real insights.

7. **Markdown Report Generation**  
   The analysis output is formatted as a markdown string, which can be saved as a `.md` file for reporting or viewing in a markdown editor.

8. **Clean Code Structure**  
   The code is modular, with separate files for:
   - Route definitions
   - Authentication and security
   - Input validation
   - Market data processing and report generation

9. **Environment Configuration**  
   Sensitive values like the token and API keys are managed using a `.env` file, which is excluded from version control via `.gitignore`.

10. **API Documentation**  
    Automatic API documentation is available via FastAPI’s Swagger UI, which helps with understanding and testing the endpoint directly in the browser.

## Files and Their Purpose

- `main.py`: App entry point, FastAPI server configuration, middleware setup.
- `.env`: Stores secret token and (optionally) Gemini API key.
- `requirements.txt`: Lists all Python packages needed to run the app.
- `routes.py`: Defines the `/analyze/{sector}` route and connects logic.
- `auth.py`: Validates Bearer token for secure access.
- `validator.py`: Ensures sector input is valid and safe.
- `analyzer.py`: Simulates market data fetching and AI-powered insight generation.
- `README.md`: This file, describing the project and instructions.

## Usage Flow

1. A client sends a GET request to `/analyze/{sector}` with a valid token.
2. The server validates the token and input.
3. The server simulates fetching sector-specific market data.
4. An AI-like process generates insights based on that data.
5. The server returns a structured report in markdown format.

## Summary

This project demonstrates a well-structured, secure, and scalable Python web API with all expected real-world backend components: authentication, rate limiting, modular design, and documentation. The AI functionality is designed to be swapped out with real services like Gemini when needed.