
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
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_id = member.get("id", self._generateId())
        member["id"] = member_id
        self._members.append(member)

    def delete_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                self._members.remove(member)
                return

    def update_member(self, member_id, updated_member):
        for i, member in enumerate(self._members):
            if member["id"] == member_id:
                self._members[i] = updated_member
                return

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member

    def get_all_members(self):
        return self._members
