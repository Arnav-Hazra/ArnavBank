import tornado.web
import json

class GetTransaction(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register

    def post(self):
        try:
            account_no = int(self.get_body_argument('account_no'))
            transactions = self.register.get_Transaction(account_no)
            self.set_header('Content-Type', 'text/html')  # Serve as HTML

            if transactions:
                response = {
                    "Account_no": account_no,
                    "Transactions": transactions
                }
                # Convert the JSON response to a pretty-printed string
                formatted_json = json.dumps(response, indent=4).replace("\n", "<br>").replace(" ", "&nbsp;")

                # HTML content including the JSON response and a back button
                html_content = f"""
                <html>
                <head>
                    <title>Transaction Results</title>
                </head>
                <body>
                    <h1>Transaction Results</h1>
                    <pre>{formatted_json}</pre>
                    <br>
                    <button onclick="window.history.back()">Go Back</button>
                </body>
                </html>
                """
                self.write(html_content)
            else:
                self.set_status(404)
                self.write("""
                <html>
                <head>
                    <title>No Transactions Found</title>
                </head>
                <body>
                    <h1>No transactions found for this account.</h1>
                    <button onclick="window.history.back()">Go Back</button>
                </body>
                </html>
                """)
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
