customer={'name':'Extreme',
          'is_verified':True}
print('Getting the mapped value to the key dictionary[key],dictionary.get(key )')
print(customer['name'])
print(customer.get('name'))
print('Trying the not existing key returns error,we can add new data as dictionary(key,value)')
print(customer.get('Type','Networking'))
