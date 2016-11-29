# coding=utf-8
"""Teste de validação de armazenamento no cache."""
import unittest

class TestEquipment(unittest.TestCase):
    """Classe de teste de equipamentos do cache/DB."""
    _equipment = Equipment()
    _ir = 3781220677092207

    def test_get_equipment_from_db(self):
        """Recupera equipamento do banco de dados."""
        e = self._equipment.get(
            key_id=self._ir, values={'ir': self._ir}, use_cache=False
        )
        self.assertEqual(type(e), dict)

    def test_save_and_get_equipment_from_cache(self):
        """Salva e recupera equipamento do cache."""
        obj = {'value': 123}
        cached_obj, expire_obj = self._equipment.save(
            info=obj, key_id=obj.get('value')
        )
        self.assertEqual(cached_obj, True)
        self.assertEqual(expire_obj, True)
        e = self._equipment.is_cached(key_id=obj.get('value'))
        self.assertEqual(e.get('value'), 123)

    def test_auto_casting_float(self):
        """Testa conversão de string para float."""
        self.assertEqual(
            type(self._equipment.cast_value('12.3')), float
        )
        self.assertNotEqual(
            type(self._equipment.cast_value('12,3')), float
        )

    def test_auto_casting_string(self):
        """Testa se conversão mantem string."""
        self.assertEqual(
            type(self._equipment.cast_value('String')), str
        )
        self.assertNotEqual(
            type(self._equipment.cast_value('"123"')), int
        )

    def test_auto_casting_integer(self):
        """Testa conversão de string para inteiro."""
        self.assertEqual(
            type(self._equipment.cast_value('123')), int
        )
        self.assertNotEqual(
            type(self._equipment.cast_value('1"23')), int
        )

    def test_auto_casting_boolean(self):
        """Testa conversão de string para boolean"""
        self.assertEqual(
            type(self._equipment.cast_value('True')), bool
        )
        self.assertEqual(
            type(self._equipment.cast_value('False')), bool
        )
        self.assertNotEqual(
            type(self._equipment.cast_value('true')), bool
        )
