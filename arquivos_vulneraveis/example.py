# vulnerable_examples/example.py
def login(user_input):
    # Simulated SQL injection vulnerability: concatenation of user input into query
    query = "SELECT * FROM users WHERE username = '" + user_input + "';"
    print("Executing query:", query)
    return query

if __name__ == "__main__":
    # Example of vulnerable call
    login("admin'; DROP TABLE users; --")
