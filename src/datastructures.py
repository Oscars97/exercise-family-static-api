
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
           {
            "id": self._generateId(),
            "first_name": 'Oscar',
            "last_name": self.last_name,
            "age": 23,
            "lucky_numbers": [7]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append({
            "id": self._generateId(),
            "first_name": member['first_name'],
            "last_name": self.last_name,
            "age": member['age'],
            "lucky_numbers": member["lucky_numbers"]
        })
        pass

    def delete_member(self, id):
        for x in self._members:
            if x['id']== id:
                self._members.remove(x)
                return self._members
        pass

    def get_member(self, id):
        print(id)
        for x in self._members:
            if x['id'] == id:
                return x
            else: 
                return x['id']
        # pass
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
