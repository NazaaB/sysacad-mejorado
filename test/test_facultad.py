import unittest
from app import create_app, db
from app.models.facultad import Facultad  

class FacultadModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_crear_facultad(self):
        facultad = Facultad(nombre="Facultad Regional San Rafael")
        db.session.add(facultad)
        db.session.commit()

        resultado = Facultad.query.filter_by(nombre="Facultad Regional San Rafael").first()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Facultad Regional Buenos Aires")

if __name__ == '__main__':
    unittest.main()
