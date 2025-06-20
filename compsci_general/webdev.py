"""
Client
"""
"""🧠 Think: 'The requester--show me a website.'"""
# The client is the user-facing part of an application.
# It sends requests to servers and displays the results.
# Runs in a browser, mobile app, or desktop app.
# Examples: Chrome, React app, iOS app, Postman

"""
Server
"""
"""🧠 Think: 'The answerer — the one who receives and responds.'"""
# The server listens for client requests and sends back data or pages.
# Often includes business logic and connects to databases.
# Runs on a remote machine or cloud instance.
# Examples: Flask, Express, Django, FastAPI

"""
Service
"""
"""🧠 Think: 'The specialist — focused on one job, callable by others.'"""
# A service performs a specific task, like authentication or payment.
# Can be part of a server or a separate microservice.
# Examples: Stripe API, Auth0, Email sending service

"""
Example Flow
"""
"""🧠 Think: 'Client asks, Server responds, Service helps behind the scenes.'"""
# 1. Client → sends HTTP request (GET /profile)
# 2. Server → processes it, may call other services
# 3. Service → does a job (e.g., fetch user data)
# 4. Server → sends back response to client
# 5. Client → renders the result for the user

"""
Quick Summary Table
"""
"""🧠 Use this to anchor the mental model."""

# Term     | Role                 | Runs on         | Examples
# ------------------------------------------------------------------
# Client   | Sends requests        | Browser/app     | Chrome, React, iOS app
# Server   | Responds to client    | Remote machine  | Fastapi, Django, Express
# Service  | Specialized logic     | Container/cloud | Stripe API, Auth0, AWS Lambda




"""
🧠A hook is like a scheduled interruption: when X happens, do Y.
"""
# Hooks are functions that run automatically at specific moments in a lifecycle.
# Example: useEffect(() => {
#   console.log("Component mounted");
# }, []);... runs when component loads

"""
🧠"Webhooks = reverse API calls."
Instead of asking, you get told when things happen.
"""
# You give an app (e.g. Stripe, GitHub) a callback URL.
# That app sends a POST request to your URL when an event occurs.
# Your server handles it.

