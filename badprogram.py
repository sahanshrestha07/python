

#Prompt the user to enter the year, make, and model of their vehicle year int(input('Please enter the model year of your vehicle: '))
year = int(input("Enter a year: "))
make = int(input('Please enter the maker of your vehicle: '))
model = input('Please enter the model of your vehicle: ')

#Generate the 3-Letter prefix: Can be A-Z

letter_a= chr(random.randint(65, 90))
letter_b = chr(random.randint(65, 90))
letter_c= chr(random.randint(65, 90))

#Generate the 4-digit number for the License plate digits random.randint(1000, 9999)

license_plate = letter_a + letter_b + letter_c + str(digits)

car {
'Year': year,
'Make': make,
'Model': model,
'Plate': license_plate
}

print(f'The license plate for your (car["Year"]) (car["Make"]} {car["Model"]) is (car["Plate"]}')