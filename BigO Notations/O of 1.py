#O(1)

#Lists

account_ids = [12,32,43,123,89,67] # Existing account holder account_ids

# O(1)
# will be a constant time operation such as appending to a list which happens to the end of list, In real situation is is like a new person opens a new account wil account account_ids
#and there will also be a situation when we want to remove the last person will pop him/her out

print(account_ids)
print(account_ids[3]) #constant time because it is directly going to 3rd location and pulling its value which will be 123 currently
account_ids[4] = 90 #this will also be a constant operation as the values gets updated in place
account_ids.append(66)# this will be a constant operation as append will add to the end no furtehr shifting to the right
account_ids.insert(3,231)  # this will not be a constant operation as it will shift value to right
print(account_ids)

popped_item = account_ids.pop() #again contant as will happen to the end

print(popped_item)
print(account_ids)




#Hashmap or Dict as you say in python

name_and_roll = {
  "om": 21,
  "sony": 32,
  "jojo": 13
}

print(name_and_roll['om']) # constant operation a sit prints the value of key
print('sony' in name_and_roll) # contant operation as lookup
name_and_roll['om'] = 99 #constant
name_and_roll['ola'] = 67 #contant
name_and_roll.pop("ola")
print(name_and_roll)

