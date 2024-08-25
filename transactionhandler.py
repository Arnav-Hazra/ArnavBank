import tornado.web

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

            # Modernized HTML content including the transaction result
            html_content = f"""
            <html>
            <head>
                <title>Transaction Added</title>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f3f4f6;
                        color: #333333;
                        margin: 0;
                        padding: 20px;
                        text-align: center;
                    }}
                    h1 {{
                        color: #003366;
                        font-size: 2.2em;
                        margin-bottom: 20px;
                    }}
                    p {{
                        font-size: 1.2em;
                        margin-bottom: 30px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 1.1em;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        max-width: 500px;
                        margin: 50px auto;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Transaction Added Successfully</h1>
                    <p>{result}</p>
                    <button onclick="window.history.back()">Go Back</button>
                </div>
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
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f3f4f6;
                        color: #333333;
                        margin: 0;
                        padding: 20px;
                        text-align: center;
                    }}
                    h1 {{
                        color: #c0392b;
                        font-size: 2.2em;
                        margin-bottom: 20px;
                    }}
                    p {{
                        font-size: 1.2em;
                        margin-bottom: 30px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 1.1em;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        max-width: 500px;
                        margin: 50px auto;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Error: {str(e)}</h1>
                    <button onclick="window.history.back()">Go Back</button>
                </div>
            </body>
            </html>
            """)
        except tornado.web.MissingArgumentError as e:
            self.set_status(400)
            self.write(f"""
            <html>
            <head>
                <title>Error</title>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f3f4f6;
                        color: #333333;
                        margin: 0;
                        padding: 20px;
                        text-align: center;
                    }}
                    h1 {{
                        color: #c0392b;
                        font-size: 2.2em;
                        margin-bottom: 20px;
                    }}
                    p {{
                        font-size: 1.2em;
                        margin-bottom: 30px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 1.1em;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                    .container {{
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        max-width: 500px;
                        margin: 50px auto;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Missing Argument: {str(e)}</h1>
                    <button onclick="window.history.back()">Go Back</button>
                </div>
            </body>
            </html>
            """)
        except Exception as e:
            self.set_status(500)
            self.write("""
            <html>
            <head>
                <title>Internal Server Error</title>
                <style>
                    body {
                        font-family: 'Arial', sans-serif;
                        background-color: #f3f4f6;
                        color: #333333;
                        margin: 0;
                        padding: 20px;
                        text-align: center;
                    }
                    h1 {
                        color: #c0392b;
                        font-size: 2.2em;
                        margin-bottom: 20px;
                    }
                    p {
                        font-size: 1.2em;
                        margin-bottom: 30px;
                    }
                    button {
                        background-color: #007bff;
                        color: white;
                        padding: 12px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 1.1em;
                        cursor: pointer;
                        transition: background-color 0.3s ease;
                    }
                    button:hover {
                        background-color: #0056b3;
                    }
                    .container {
                        background-color: #ffffff;
                        border-radius: 10px;
                        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                        padding: 30px;
                        max-width: 500px;
                        margin: 50px auto;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Internal Server Error</h1>
                    <button onclick="window.history.back()">Go Back</button>
                </div>
            </body>
            </html>
            """)
            raise e  # Optionally log or re-raise the error
