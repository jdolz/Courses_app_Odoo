# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase


class TestCourses(TransactionCase):
    def test_create(self):
        "Create a simple Course"
        Courses = self.env['courses.course']
        course = Courses.create({'name': 'Test Course'})
        self.assertEqual(course.is_done, False)
