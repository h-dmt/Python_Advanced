from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Mario', {"linear algebra 2": ["Matrix operation", "Fourier Transformation"]})

    def test_constructor(self):
        self.assertEqual(self.student.name, "Mario")
        self.assertEqual(self.student.courses, {"linear algebra 2": ["Matrix operation", "Fourier Transformation"]})
        student2 = Student("Roberto")
        self.assertEqual(student2.courses, {})

    def test_enroll_course_exsisting_note_add(self):
        result = self.student.enroll("linear algebra 2", ["Fourier Inverse"])
        result2 = self.student.enroll("linear algebra 2", ["note"], 'Y')
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(result2, "Course already added. Notes have been updated.")

    def test_enroll_course_exsistent_note_added_check(self):
        self.student.enroll("linear algebra 2", ["Fourier Inverse"])
        self.assertEqual(self.student.courses["linear algebra 2"][2], "Fourier Inverse")

    def test_enroll_add_course_and_add_notes(self):
        result = self.student.enroll("course 2", ["note_1", "note_2"], "Y")
        result2 = self.student.enroll("course 3", ["note_1", "note_2"])
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(result2, "Course and course notes have been added.")

    def test_enroll_add_course_and_notes_check_added(self):
        self.student.enroll("course 2", ["note_1", "note_2"], "Y")
        self.assertEqual((self.student.courses["course 2"]), ["note_1", "note_2"])

    def test_enroll_add_only_course(self):
        result = self.student.enroll("course 2", ['note'], "N")
        self.assertEqual(result, "Course has been added.")

    def test_enroll_add_only_course_added_to_dictionary(self):
        self.student.enroll("course 2", ['note'], "N")
        self.assertEqual(self.student.courses["course 2"], [])

    def test_add_notes(self):
        result = self.student.add_notes("linear algebra 2", "exam prep")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(self.student.courses["linear algebra 2"][-1], "exam prep")

    def test_add_note_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("linear algebra 3", "ODEs")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_course_removed(self):
        result = self.student.leave_course("linear algebra 2")
        self.assertEqual(result, "Course has been removed")

    def test_leave_course_removed_from_dictionary(self):
        self.student.leave_course("linear algebra 2")
        self.assertEqual(self.student.courses, {})

    def test_leave_course_not_found(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("math")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == "__main__":
    main()
