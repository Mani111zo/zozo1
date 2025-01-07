class School(Document):
    students = ListField(ReferenceField('Student'))

    def add_student(student):
        School.objects(id=self.id).update_one(push__students=student.id)
        