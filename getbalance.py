import tornado.web
import json

class GetBalance(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register

    def post(self):
        try:
            total_balance = self.register.get_Total_Balance()  # Fetch the total balance across all accounts
            self.set_header('Content-Type', 'text/html')  # Serve as HTML

            # HTML content formatted to resemble a modern bank app's UI
            html_content = f"""
            <html>
            <head>
                <title>Bank Total Balance</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f7f6;
                        margin: 0;
                        padding: 0;
                        text-align: center;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        margin: 50px auto;
                        max-width: 400px;
                    }}
                    h1 {{
                        color: #2d3e50;
                    }}
                    p {{
                        font-size: 18px;
                        color: #4f5b66;
                    }}
                    .balance {{
                        font-size: 32px;
                        font-weight: bold;
                        color: #27ae60;
                    }}
                    .back-btn {{
                        background-color: #3498db;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-size: 16px;
                    }}
                    .back-btn:hover {{
                        background-color: #2980b9;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Bank Total Balance</h1>
                    <p>The total balance available in the bank is</p>
                    <p class="balance">Rs: {total_balance:.2f}</p>
                    <br>
                    <button class="back-btn" onclick="window.history.back()">Go Back</button>
                </div>
            </body>
            </html>
            """
            self.write(html_content)
        except Exception as e:
            self.set_status(500)
            self.write("""
            <html>
            <head>
                <title>Internal Server Error</title>
            </head>
            <body>
                <h1>Internal server error.</h1>
                <button onclick="window.history.back()">Go Back</button>
            </body>
            </html>
            """)
            raise e  # Optionally log or re-raise the error
