from copy import copy

class Students:
    """A database that contains students."""
    def __init__(self):
        self.db = {}
        self.counter = 1

    def new(self, name):
        """Adds a new student to the students database. This creates a record of the form {"name": name} and assigns
        it a generated student ID.

        @param str name: The name of the student.
        @return int: The student ID.
        """
        if self.counter > 9999:
            raise RuntimeError("Student ID limit reached. Student IDs must not be larger than 9999.")
        self.create(self.counter, {"name": name})
        self.counter += 1
        return self.counter - 1

    def has_key(self, key):
        """Checks whether a record exists for the given key.

        @param key: A key.
        @return bool: Whether the record exists.
        """
        return key in self.db

    def create(self, key, record, overwrite=False):
        """Creates a record stored under the given key. If overwrite is True, this method will overwrite any existing
        record with this key.

        @param key: A key.
        @param dict record: A record to store under this key.
        @param bool overwrite: Whether to overwrite an existing entry.
        @raise ValueError: If the key already exists, and overwrite is not True.
        """
        if key in self.db and not overwrite:
            raise ValueError("A record for key \"%s\" already exists." % key)
        self.db[key] = copy(record)

    def read(self, key):
        """Fetches a record from the database with the given key, raising a LookupError if no record was found.

        @param key: The key.
        @return dict: The found record.
        @raise LookupError: If the record wasn't found.
        """
        if key not in self.db:
            raise LookupError("No record for key \"%s\" exists." % key)
        return self.db[key]

    def try_read(self, key):
        """Fetches a record from the database with the given key, returning None if no record was found.

        @param key: The key.
        @return dict | None: The record, or None if no record was found.
        """
        if key not in self.db:
            return None
        return self.db[key]

    def update(self, key, data, overwrite=False):
        """Updates the record under the given key.
        If overwrite is False, then the entries in the data hash will be written to the record.
        If overwrite is True, then the record will be overwritten with a copy of the data hash.

        @param key: The key.
        @param hash data: A hash that will be merged onto the record, or copied to replace it.
        @param bool overwrite: Whether to overwrite the record or simply update it.
        @return hash: The new record.
        @raise LookupError: If the record wasn't found.
        """
        if key not in self.db:
            raise LookupError("No record for key \"%s\" exists." % key)

        if overwrite:
            self.db[key] = copy(data)
        else:
            record = self.db[key]
            for k, v in data.items():
                record[k] = data[k]

        return self.db[key]

    def delete(self, key):
        """Deletes the record under the given key.

        :param key: The key.
        :return hash: The deleted record.
        :raise LookupError: If the record wasn't found.
        """
        if key not in self.db:
            raise LookupError("No record for key \"%s\" exists." % key)

        record = self.db[key]
        del self.db[key]
        return record


def main():
    students = Students()
    wendy_id = students.new(name="Wendy Wacko")
    justin_id = students.new(name="Justin Case")
    terry_id = students.new(name="Terry Bull")
    stan_id = students.new(name="Stan Still")

    print("Student with invalid ID 9999: %s" % students.try_read(9999))
    for id in [wendy_id, justin_id, terry_id, stan_id]:
        print("Student with ID %04d: %s" % (id, students.read(id)))

    students.update(justin_id, {"name": "Mark Post"})
    print("Justin Case (0002)'s new name after joining the witness protection program: %s" % students.read(justin_id))

    students.delete(wendy_id)
    print("Querying for Wendy Wacko's ID (0001) after deleting the record yields: %s" % students.try_read(wendy_id))

    macon_id = students.new("Macon Paine")
    print("Freshly created student Macon Paine has ID %04d." % macon_id)

if __name__ == "__main__":
    main()