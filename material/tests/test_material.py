from odoo.tests import common
from odoo.exceptions import UserError


class TestMaterial(common.TransactionCase):
    def setUp(self):
        super(TestMaterial, self).setUp()
        self.partner = self.env['res.partner']
        # Set up any necessary test data here
        self.supplier = self.partner.create({
            'name': 'Nigel',
            'city': 'Birmingham',
            'zip': 'B46 3AG',
            'street': 'Cannon Hill Park'
        })

        self.customer = self.env['res.partner'].create({
            'name': 'Nigel Park',
            'city': 'Birmingham',
            'zip': 'B46 3AG',
            'street': 'Cannon Hill Park',
        })


    def test_create_material(self):
        record = self.env['material.material'].create(
            {
                'name': 'Test A',
                'material_code': 'TESTCODE',
                'material_type': '1',
                'buy_price': 200,
                'supplier_id': self.supplier.id,
            }
        )

        self.assertEqual(record.name, 'Test A')
        self.assertEqual(record.material_code, 'TESTCODE')
        self.assertEqual(record.material_type, '1')
        self.assertEqual(record.buy_price, 200)
        self.assertEqual(record.supplier_id.id, self.supplier.id)

    def test_create_material_error(self):
        with self.assertRaises(UserError, msg='Buy Price must be greater than 100'):
            self.env['material.material'].create(
                {
                    'name': 'Test A',
                    'material_code': 'TESTCODE',
                    'material_type': '1',
                    'buy_price': 99,
                    'supplier_id': self.customer.id,
                }
            )

    def test_update_material(self):
        record = self.env['material.material'].create(
            {
                'name': 'Test A',
                'material_code': 'TESTCODE',
                'material_type': '1',
                'buy_price': 200,
                'supplier_id': self.supplier.id,
            }
        )
        self.assertEqual(record.name, 'Test A')
        record.write({
            'name': 'Test B',
        })
        self.assertEqual(record.name, 'Test B')

    def test_delete_material(self):
        record = self.env['material.material'].create(
            {
                'name': 'Test A',
                'material_code': 'TESTCODE',
                'material_type': '1',
                'buy_price': 200,
                'supplier_id': self.supplier.id,
            }
        )
        self.assertEqual(record.search_count([('material_code', '=',
                                               'TESTCODE')]), 1)

        record.unlink()
        self.assertEqual(record.search_count([('material_code', '=',
                                               'TESTCODE')]), 0)

    def test_material_buy_price_less_than_100(self):
        with self.assertRaises(UserError, msg='Buy Price must be greater than 100'):
            self.env['material.material'].create(
                {
                    'name': 'Test A',
                    'material_code': 'TESTCODE',
                    'material_type': '1',
                    'buy_price': 99,
                    'supplier_id': self.supplier.id,
                }
            )
    def test_material_buy_price_is_zero(self):
        with self.assertRaises(UserError, msg='Buy Price must be greater than 100'):
            self.env['material.material'].create(
                {
                    'name': 'Test A',
                    'material_code': 'TESTCODE',
                    'material_type': '1',
                    'buy_price': 0.0,
                    'supplier_id': self.supplier.id,
                }
            )