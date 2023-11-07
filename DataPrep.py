#!/usr/bin/env python
# coding: utf-8

# ## Data Prep

# ### Integer data

# In[1]:


import csv
import random

# Set the number of rows and the filename
num_rows = 203100
filename = 'int02mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[2]:


# Set the number of rows and the filename
num_rows = 203100
filename = 'int02mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[3]:


# Set the number of rows and the filename
num_rows = 395000
filename = 'int04mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[4]:


# Set the number of rows and the filename
num_rows = 395000
filename = 'int04mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[5]:


# Set the number of rows and the filename
num_rows = 779600
filename = 'int08mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[6]:


# Set the number of rows and the filename
num_rows = 779600
filename = 'int08mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[7]:


# Set the number of rows and the filename
num_rows = 1510000
filename = 'int16mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[8]:


# Set the number of rows and the filename
num_rows = 1510000
filename = 'int16mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = random.randint(0, 100)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# ### Decimal data

# In[9]:


import csv
import random

# Set the number of rows and the filename
num_rows = 160500
filename = 'dec02mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[10]:


# Set the number of rows and the filename
num_rows = 160500
filename = 'dec02mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[11]:


# Set the number of rows and the filename
num_rows = 312000
filename = 'dec04mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[12]:


# Set the number of rows and the filename
num_rows = 312000
filename = 'dec04mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[13]:


# Set the number of rows and the filename
num_rows = 616000
filename = 'dec08mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[14]:


# Set the number of rows and the filename
num_rows = 616000
filename = 'dec08mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[15]:


# Set the number of rows and the filename
num_rows = 1210000
filename = 'dec16mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# In[16]:


# Set the number of rows and the filename
num_rows = 1210000
filename = 'dec16mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        value = round(random.uniform(0, 100), 2)
        # Write the data to the CSV file
        csvwriter.writerow([id, value])


# ### Text data

# In[17]:


import csv
import random
import string

# Set the number of rows and the filename
num_rows = 13350
filename = 'text02mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[18]:


# Set the number of rows and the filename
num_rows = 13350
filename = 'text02mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[19]:


# Set the number of rows and the filename
num_rows = 26650
filename = 'text04mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[20]:


# Set the number of rows and the filename
num_rows = 26650
filename = 'text04mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[21]:


# Set the number of rows and the filename
num_rows = 53180
filename = 'text08mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[22]:


# Set the number of rows and the filename
num_rows = 53180
filename = 'text08mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[23]:


# Set the number of rows and the filename
num_rows = 106600
filename = 'text16mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# In[24]:


# Set the number of rows and the filename
num_rows = 106600
filename = 'text16mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random text string with length between 100 and 200 characters
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(100, 200)))
        # Write the data to the CSV file
        csvwriter.writerow([id, text])


# ### JSON_CSV data

# In[25]:


import csv
import json
import random
import string

# Set the number of rows and the filename
num_rows = 25000
filename = 'json02mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[26]:


# Set the number of rows and the filename
num_rows = 25000
filename = 'json02mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[27]:


# Set the number of rows and the filename
num_rows = 49800
filename = 'json04mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[28]:


# Set the number of rows and the filename
num_rows = 49800
filename = 'json04mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[29]:


# Set the number of rows and the filename
num_rows = 99300
filename = 'json08mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[30]:


# Set the number of rows and the filename
num_rows = 99300
filename = 'json08mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[31]:


# Set the number of rows and the filename
num_rows = 198000
filename = 'json16mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# In[32]:


# Set the number of rows and the filename
num_rows = 198000
filename = 'json16mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random JSON object with 5 key-value pairs
        json_data = {}
        for j in range(5):
            key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            value = random.randint(1, 100)
            json_data[key] = value
        # Convert the JSON object to a string
        json_string = json.dumps(json_data)
        # Write the data to the CSV file
        csvwriter.writerow([id, json_string])


# ### Geometry data

# In[33]:


import csv
import random

# Set the number of rows and the filename
num_rows = 70400
filename = 'geo02mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[34]:


# Set the number of rows and the filename
num_rows = 70400
filename = 'geo02mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[35]:


# Set the number of rows and the filename
num_rows = 138800
filename = 'geo04mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[36]:


# Set the number of rows and the filename
num_rows = 138800
filename = 'geo04mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[37]:


# Set the number of rows and the filename
num_rows = 273800
filename = 'geo08mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[38]:


# Set the number of rows and the filename
num_rows = 273800
filename = 'geo08mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[39]:


# Set the number of rows and the filename
num_rows = 547000
filename = 'geo16mb01.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])


# In[40]:


# Set the number of rows and the filename
num_rows = 547000
filename = 'geo16mb02.csv'

# Open the file for writing
with open(filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    # Write the header row
    csvwriter.writerow(['id', 'value'])
    # Loop through the rows and generate random data
    for i in range(num_rows):
        id = i + 1
        # Generate a random latitude and longitude
        latitude = round(random.uniform(-90, 90), 6)
        longitude = round(random.uniform(-180, 180), 6)
        # Combine the latitude and longitude into a string
        geometry = str(latitude) + ',' + str(longitude)
        # Write the data to the CSV file
        csvwriter.writerow([id, geometry])

