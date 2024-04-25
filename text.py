import json

# Step 1: Create a file named "ex5.json" and save the provided JSON data.

# Step 2: Read the JSON data from the file and store it in a dictionary named "ex5".
with open("ex5.json", "r") as file:
    ex5 = json.load(file)

# Step 3: Update the "ex5" dictionary by adding a new batter named "Tea" for the donut with the name "Old Fashioned".
for donut in ex5:
    if donut["name"] == "Old Fashioned":
        donut["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

# Step 4: Write the updated dictionary back to the "ex5.json" file.
with open("ex5.json", "w") as file:
    json.dump(ex5, file, indent=4)