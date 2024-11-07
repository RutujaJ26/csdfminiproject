from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import random

# Initialize the WebDriver (make sure to replace 'path/to/chromedriver' with your actual path)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def add_task():
    try:
    # Open the To-Do app running on localhost
        driver.get("http://localhost:8090/TODO/add_todo.jsp")  # Change the port if needed

    # Wait for the page to load
        time.sleep(2)

    # Add a new task
        task_name_input = driver.find_element(By.CSS_SELECTOR, '#exampleInputEmail1[name="username"]')  # Task name input
        task_input = driver.find_element(By.CSS_SELECTOR, '#exampleInputEmail1[name="todo"]')  # Task details input
        status_dropdown = driver.find_element(By.CSS_SELECTOR, '#inputState')  # Dropdown for task status

        # Fill in the task name and details
        task_name_input.send_keys(input("Enter the task name"))
        time.sleep(2)
        task_input.send_keys(input("Enter the task description"))
        time.sleep(2)

        
        # Select the status from the dropdown
        status_dropdown.click()  # Select "Pending" status
        driver.find_element(By.XPATH, f'//*[@id="inputState"]/option[{random.randint(3, 4)}]').click()
        # Submit the task (Assuming there is a submit button with ID 'submit-task')
        submit_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        submit_button.click()

        driver.get("http://localhost:8090/TODO/index.jsp")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    # Wait for the task to be added
        
def delete_task():
    try:
        # Find the delete button
        delete_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-sm.btn-danger')
        delete_button.click()

            # Wait for the deletion to take effect
        time.sleep(2)
            
        print("Task deleted successfully.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")
        
    



add_task()
time.sleep(5)
delete_task()
driver.quit()
