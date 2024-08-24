import tornado.web
import json

class TransactionHandler(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register

    def post(self):
        try:
            account_no = int(self.get_body_argument('account_no'))
            date = self.get_body_argument('date')
            type = self.get_body_argument('type')
            amount = float(self.get_body_argument('amount'))

            # Validate the type of transaction
            if type not in ["deposit", "withdraw"]:
                raise ValueError("Invalid transaction type.")

            result = self.register.add_Transaction(account_no, date, type, amount)
            self.set_header('Content-Type', 'text/html')  # Serve as HTML

            # HTML content including the transaction result and a back button
            html_content = f"""
            <html>
            <head>
                <title>Transaction Added</title>
            </head>
            <body>
                <h1>Transaction Added Successfully</h1>
                <p>{result}</p>
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
