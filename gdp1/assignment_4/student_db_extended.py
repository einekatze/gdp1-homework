from peewee import *
from random import choice

# import logging
# logger = logging.getLogger("peewee")
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())

db = SqliteDatabase(":memory:")


class BaseModel(Model):
    class Meta:
        database = db


class Student(BaseModel):
    name = CharField()
    sid = IntegerField(unique=True, index=True)

    @classmethod
    def generate_sid(cls):
        """Generate a student ID, which is separate from the record ID.

        @return int: A generated student ID.
        @raise RuntimeError: If no student ID is available anymore.
        """
        used_ids = [res.sid for res in cls.select(cls.sid)]
        free_ids = set(range(1, 10000)) - set(used_ids)

        if len(free_ids) == 0:
            raise RuntimeError("No free student IDs are left.")

        return choice(tuple(free_ids))


class Group(BaseModel):
    desc = CharField()
    gid = IntegerField(unique=True, index=True)

    @classmethod
    def generate_gid(cls):
        """Generate a group ID, which is separate from the record ID.

        @return int: A generated group ID.
        @raise RuntimeError: If no group ID is available anymore.
        """
        used_ids = [res.gid for res in cls.select(cls.gid)]
        free_ids = set(range(1, 1000)) - set(used_ids)

        if len(free_ids) == 0:
            raise RuntimeError("No free group IDs are left.")

        return choice(tuple(free_ids))


class StudentGroup(BaseModel):
    student = ForeignKeyField(Student)
    group = ForeignKeyField(Group)

    class Meta:
        # Add a unique compound index to the table. This makes sure on the database level that students can't
        # be in the same group twice.
        indexes = (
            (("student", "group"), True),
        )


def main():
    # Create the tables in the in-memory database.
    db.create_tables([Student, Group, StudentGroup])

    # Create the individual students.
    wendy = Student.create(name="Wendy Wacko", sid=Student.generate_sid())
    justin = Student.create(name="Justin Case", sid=Student.generate_sid())
    terry = Student.create(name="Terry Bull", sid=Student.generate_sid())
    stan = Student.create(name="Stan Still", sid=Student.generate_sid())

    # Create the student groups.
    group1 = Group.create(desc="Test Group A", gid=Group.generate_gid())
    group2 = Group.create(desc="Test Group B", gid=Group.generate_gid())

    # Link the students and groups together.
    StudentGroup.create(student=wendy, group=group1)
    StudentGroup.create(student=justin, group=group1)
    StudentGroup.create(student=terry, group=group1)

    StudentGroup.create(student=terry, group=group2)
    StudentGroup.create(student=stan, group=group2)

    # This long query is responsible for fetching a list of StudentGroup entries and at the same time, fetching
    # all the student and group data that is referenced by them.
    query = (StudentGroup
        .select(StudentGroup, Student, Group)
        .join(Group)
        .switch(StudentGroup)
        .join(Student)
        .order_by(Student.id))

    # Output the groups to which students belong.
    last = None
    for student_group in query:
        student = student_group.student
        group = student_group.group

        if student != last:
            last = student
            print("%s (ID %04d) is is in the following groups:" % (student.name, student.sid))

        print("            Group %03d - %s" % (group.gid, group.desc))



if __name__ == "__main__":
    main()

# Output:
# Wendy Wacko (ID 0419) is is in the following groups:
#             Group 178 - Test Group A
# Justin Case (ID 4154) is is in the following groups:
#             Group 178 - Test Group A
# Terry Bull (ID 9586) is is in the following groups:
#             Group 178 - Test Group A
#             Group 801 - Test Group B
# Stan Still (ID 3074) is is in the following groups:
#             Group 801 - Test Group B
