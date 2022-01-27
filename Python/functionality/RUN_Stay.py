
import Stay


# Instance of Stay object
stay = Stay.Stay(total_price=2717, num_nights=7)

# Provide info on people staying
stay.AddPerson(name="Kevin",  nights_staying=[0,1,2,3,4,5,6])
stay.AddPerson(name="Mary",   nights_staying=[0,1,2,3,4,5,6])
stay.AddPerson(name="Matthew", nights_staying=[0,1,2,3,4,5,6])
stay.AddPerson(name="Amanda", nights_staying=[0,1,2,3,4,5,6])
stay.AddPerson(name="Emily",  nights_staying=[0,1,2,3,4,5,6])
stay.AddPerson(name="Omkar",  nights_staying=[4,5,6])
stay.AddPerson(name="Ansley", nights_staying=[6])

# Calculate original split-up
stay.CalculateOriginalCosts()


# Make post-trip corrections
stay.ChangePersonNights(name="Ansley", nights_staying=[4,5,6])


# Calculate Redistribution
stay.CalculateRedistribution()