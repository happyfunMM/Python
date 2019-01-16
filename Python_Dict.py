
#Create a dict:
europe1 = { 'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}
europe2 = dict(Spain = 'Madrid', France = 'Paris', Germany = 'Berlin', Norway = 'Oslo')

# Print out the keys in europe
print(europe.keys())

#Update dict:
europe2.update({'UK': 'London'})

#Delete elements:
del(europe2['Spain'])
del(europe2['UK'],europe2['France'])

#Create dicts from sequences:
mapping = {}
for key, value in zip(key_list, value_list):
    mapping[key] = value
    
mapping = dict(zip(key_list, value_list))


# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
           
# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data ={'capital':'rome', 'population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
