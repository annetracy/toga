import toga
from toga.sources import TreeSource
from toga_dummy.utils import TestCase


class TreeTests(TestCase):
    def setUp(self):
        super().setUp()

        self.headings = [f'Heading {x}' for x in range(3)]

        self.data = None
        self.tree = toga.Tree(
            headings=self.headings,
            data=self.data,
        )

    def test_widget_created(self):
        self.assertEqual(self.tree._impl.interface, self.tree)
        self.assertActionPerformed(self.tree, 'create Tree')
        self.assertIsInstance(self.tree.data, TreeSource)

        self.assertEqual(self.tree.headings, self.headings)

    def test_setter_creates_tree_with_TreeSource_data(self):
        data = {
            ('one', 1): [
                ('one.one', 1.1),
                ('one.two', 2.1)
            ],
            ('two', 2): None
        }

        accessors = [f'heading{i}' for i in range(3)]

        self.tree.data = TreeSource(data=data, accessors=accessors)

        self.assertIsInstance(self.tree.data, TreeSource)
        self.assertEqual(self.tree.data[0].heading0, 'one')
        self.assertEqual(self.tree.data[0][0].heading1, 1.1)
        self.assertEqual(self.tree.data[1].heading1, 2)

    def test_setter_creates_tree_with_dict_data(self):
        self.data = {
            ('first', 111): None,
            ('second', 222): [],
            ('third', 333): [
                ('third.one', 331),
                {'heading_0': 'third.two', 'heading_1': 332}
            ]
        }
        self.tree.data = self.data

        self.assertIsInstance(self.tree.data, TreeSource)
        self.assertFalse(self.tree.data[0].can_have_children())
        self.assertTrue(self.tree.data[1].can_have_children())
        self.assertEqual(self.tree.data[1].heading_1, 222)
        self.assertEqual(self.tree.data[2][0].heading_1, 331)

    def test_data_setter_creates_tree_with_tuple_data(self):
        pass

    def test_data_setter_creates_tree_with_list_data(self):
        pass

    def test_data_setter_creates_tree_with_data_source(self):
        pass

    def test_data_setter_creates_tree_with_data_none(self):
        pass

    def test_multiselect_getter(self):
        super().setUp()
        self.headings = [f'Heading {x}' for x in range(3)]

        self.data = None
        self.tree = toga.Tree(
            headings=self.headings,
            data=self.data,
            multiple_select=True,
        )

        self.assertEqual(self.tree.multiple_select, True)

        self.tree = toga.Tree(
            headings=self.headings,
            data=self.data,
            multiple_select=False,
        )

        self.assertEqual(self.tree.multiple_select, False)
