# 💘 Dating App – Full Stack Project (Angular + .NET)

A full-stack dating application built with Angular (frontend) and .NET (backend).
This project was created as a portfolio piece to demonstrate real-world application architecture, authentication, file uploads, and business logic implementation.

## 🚀 Features

- User registration and authentication (JWT)
- Profile creation and editing
- Photo upload
- Like system
- Match detection
- Real-time messaging (if you implement it later)

## 🔐 Authentication Flow

1. User logs in with email and password.
2. Backend validates credentials.
3. A JWT token is generated.
4. Angular stores the token.
5. HTTP Interceptor attaches the token to protected requests.

## ⚙️ Running the Project

### Backend
1. Navigate to the API folder
2. Run:
   dotnet run

### Frontend
1. Navigate to the client folder
2. Run:
   2.1: npm install
   2.2: ng serve

If you want to see the matches page, you can easily register on the app and access the page.
