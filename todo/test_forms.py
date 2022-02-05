from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})  # simulates user submitting a form with blank name field
        self.assertFalse(form.is_valid())  # test if form is not valid
        self.assertIn('name', form.errors.keys())  # test if error ocurred on the name field
        self.assertEqual(form.errors['name'][0], 'This field is required.')  # tests if error message on the field is 'This field is required.'
    
    def test_done_field_is_not_required(self):
        form = ItemForm({'name':'Test Todo Item'})
        self.assertTrue(form.is_valid())
    
    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
