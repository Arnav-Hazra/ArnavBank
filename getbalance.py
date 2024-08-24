import tornado.web
import json

class GetBalance(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register

    def post(self):
        try:
            account_no = int(self.get_body_argument('account_no'))
            balance = self.register.get_Sum(account_no)
            self.set_header('Content-Type', 'text/html')  # Serve as HTML

            # HTML content including the balance result and a back button
            html_content = f"""
            <html>
            <head>
                <title>Account Balance</title>
            </head>
            <body>
                <h1>Account Balance</h1>
                <p><strong>Account Number:</strong> {account_no}</p>
                <p><strong>Balance:</strong> ₹{balance:.2f}</p>
                <br>
                <button onclick="window.history.back()">Go Back</button>
            </body>
            </html>
            """
            self.write(html_content)
        except ValueError as e:
            self.set_status(400)
            self.write(f"""
            <html>
            <head>
                <title>Error</title>
            </head>
            <body>
                <h1>Error: {str(e)}</h1>
                <button onclick="window.history.back()">Go Back</button>
            </body>
            </html>
            """)
        except tornado.web.MissingArgumentError as e:
            self.set_status(400)
            self.write(f"""
            <html>
            <head>
                <title>Error</title>
            </head>
            <body>
                <h1>Missing argument: {str(e)}</h1>
                <button onclick="window.history.back()">Go Back</button>
            </body>
            </html>
            """)
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
