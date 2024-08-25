import tornado.web
import json

class GetTransaction(tornado.web.RequestHandler):
    def initialize(self, register):
        self.register = register

    def post(self):
        try:
            account_no = int(self.get_body_argument('account_no'))
            transactions = self.register.get_Transaction(account_no)
            balance = self.register.get_Sum(account_no)  # Retrieve the account balance

            self.set_header('Content-Type', 'text/html')  # Serve as HTML

            if transactions:
                # HTML content for displaying transactions as a passbook
                html_content = f"""
                <html>
                <head>
                    <title>Transaction Results</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f9;
                            margin: 0;
                            padding: 20px;
                            text-align: center;
                        }}
                        h1 {{
                            color: #003366;
                        }}
                        table {{
                            width: 80%;
                            margin: 20px auto;
                            border-collapse: collapse;
                        }}
                        th, td {{
                            padding: 12px;
                            border: 1px solid #ccc;
                            text-align: left;
                        }}
                        th {{
                            background-color: #007bff;
                            color: white;
                        }}
                        tr:nth-child(even) {{
                            background-color: #f2f2f2;
                        }}
                        tr:nth-child(odd) {{
                            background-color: #ffffff;
                        }}
                        button {{
                            background-color: #007bff;
                            color: white;
                            padding: 10px 20px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                            margin-top: 20px;
                        }}
                        button:hover {{
                            background-color: #0056b3;
                        }}
                        .balance-row td {{
                            font-weight: bold;
                            background-color: #e0e0e0;
                        }}
                    </style>
                </head>
                <body>
                    <h1>Transaction Records For</h1>
                    <h1>Account Number: {account_no}</h1>
                    <table>
                        <tr>
                            <th>Date</th>
                            <th>Type</th>
                            <th>Amount</th>
                        </tr>
                """

                # Append each transaction as a table row, assuming transaction is a tuple
                for transaction in transactions:
                    html_content += f"""
                    <tr>
                        <td>{transaction[1]}</td>  <!-- Date -->
                        <td>{transaction[2]}</td>  <!-- Type -->
                        <td>{transaction[3]}</td>  <!-- Amount -->
                    </tr>
                    """

                # Add the balance row at the end
                html_content += f"""
                    <tr class="balance-row">
                        <td colspan="2">Account Balance</td>
                        <td>{balance:.2f}</td>
                    </tr>
                    </table>
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
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            text-align: center;
                            margin: 20px;
                        }}
                        button {{
                            background-color: #007bff;
                            color: white;
                            padding: 10px 20px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                        }}
                        button:hover {{
                            background-color: #0056b3;
                        }}
                    </style>
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
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin: 20px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                </style>
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
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin: 20px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                </style>
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
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                        margin: 20px;
                    }}
                    button {{
                        background-color: #007bff;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <h1>Internal server error.</h1>
                <button onclick="window.history.back()">Go Back</button>
            </body>
            </html>
            """)
            raise e  # Optionally log or re-raise the error
